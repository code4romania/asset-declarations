import pytest

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_template.utils import AutoCleanModelMixin, XORModelMixin


class DummyModel(AutoCleanModelMixin, XORModelMixin, models.Model):
    class Meta:
        abstract = True

    def __init__(self, fields, *args, **kwargs):
        self.XOR_FIELDS = fields
        for group in fields:
            for field in group:
                setattr(self, field, "")
        super().__init__(*args, **kwargs)


@pytest.mark.parametrize("commune, city, village", [("", "", ""), ("x", "y", "z"), (0, False, ""),])
def test_xor_errors(commune, city, village):
    """ Should raise ValidationError if no field has a value or all fields are dirty."""

    model = DummyModel([{"commune": _("commune"), "city": _("city"), "village": _("village"),}])

    model.commune = commune
    model.city = city
    model.village = village

    with pytest.raises(ValidationError) as err:
        model.save()

    assert "Foloseste doar unul din urmatoarele campuri: comuna, oras" in str(err)


@pytest.mark.parametrize("commune, city, village", [("a", "", ""), ("", 0, ""), ("", "", False),])
def test_xor(commune, city, village):
    """ Shouldn't raise any ValidationErrors for false values. """

    model = DummyModel([{"commune": _("commune"), "city": _("city"), "village": _("village"),}])
    model.commune = commune
    model.city = city
    model.village = village
    model.full_clean()


def test_multiple_xors():
    """ Raise just one ValidationError for multiple xor errors. """

    model = DummyModel(
        [
            {"commune": _("commune"), "city": _("city"), "village": _("village"),},
            {"lender": _("lender"), "person": _("person"),},
        ]
    )

    with pytest.raises(ValidationError) as err:
        model.save()

    assert "Foloseste doar unul din urmatoarele campuri: comuna, oras, sat" in str(err)
    assert "Foloseste doar unul din urmatoarele campuri: creditor, persoana" in str(err)
