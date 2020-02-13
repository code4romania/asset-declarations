from django.core.exceptions import ValidationError
from django.utils.text import format_lazy
from django.utils.translation import ugettext_lazy as _


class AutoCleanModelMixin:
    def _init_states(self):
        self.initial_state = self.current_state

        self.cleaned_state = {} if not getattr(self, 'pk', None) else self.initial_state.copy()
        self.saved_state = {} if not getattr(self, 'pk', None) else self.initial_state.copy()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_states()

    @property
    def current_state(self):
        return {
            field.name: self.__dict__[field.attname]
            for field in (self._meta.fields if hasattr(self, '_meta') else [])
            if field.attname in self.__dict__
        }

    @staticmethod
    def _states_diff(state, other_state):
        return {key: value for key, value in other_state.items() if value != state[key]}

    def get_dirty_fields(self):
        return self._states_diff(self.current_state, self.cleaned_state)

    def get_unsaved_fields(self):
        if not self.saved_state:
            return list(self.current_state.keys())
        return list(self._states_diff(self.current_state, self.saved_state).keys())

    @property
    def is_cleaned(self):
        if not getattr(self, ".cleaned", False):
            return False

        return not self.get_dirty_fields()

    @is_cleaned.setter
    def is_cleaned(self, value):
        if value:
            self.cleaned_state = self.current_state.copy()

        setattr(self, ".cleaned", value)

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()

        super().save(*args, **kwargs)

        self.initial_state = self.current_state.copy()
        if "update_fields" not in kwargs:
            self.saved_state = self.current_state.copy()
        else:
            for field in kwargs["update_fields"]:
                self.saved_state[field] = self.current_state[field]

    def refresh_from_db(self, *args, **kwargs):
        super().refresh_from_db(*args, **kwargs)

        self._init_states()

    def full_clean(self, *args, **kwargs):
        if self.is_cleaned:
            return

        super().full_clean(*args, **kwargs)

        self.is_cleaned = True


class XORModelMixin:
    """
    Certain fields, like commune and city, are mutually exclusive, meaning that those can't be all None or both filled.

    To use this mixin, the class needs to have a XOR_FIELDS attribute that represents a list of dicts, containing
    mutually exclusive fields as keys and their translation as values.

    XOR_FIELDS = [
        {
            "commune": _("commune"),
            "city": _("city"),
        }
    ]

    """

    XOR_FIELDS = []

    def full_clean(self, *args, **kwargs):
        super().full_clean(*args, **kwargs)
        error_msg = _("Use only one of the following fields: ")

        errors = []

        for group in self.XOR_FIELDS:
            dirty = []

            for field in group:
                if not hasattr(self, field):
                    errors.append(_(f"Invalid field name {field}"))
                    continue

                field_value = getattr(self, field, None)
                if field_value in ["", None]:
                    dirty.append(field)

            if not dirty or len(dirty) != 1:
                # https://docs.djangoproject.com/en/2.0/topics/i18n/translation/#formatting-strings-format-lazy
                # Combine i18n fields with the error message: {error_msg} {commune} {city}
                error_fmt = format_lazy("{error_msg}" + ', '.join(["{" + field + "}" for field in group]),
                                        error_msg=error_msg, **group)
                errors.append(error_fmt)

        if errors:
            raise ValidationError(errors)
