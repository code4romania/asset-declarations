import pytest

from django.core.exceptions import ValidationError

from project_template.utils import AutoCleanModelMixin


class MockModelWithCustomValidation:
    def __init__(self, error):
        self.error = error

    def full_clean(self, *args, **kwargs):
        raise self.error


class DummyModel(AutoCleanModelMixin, MockModelWithCustomValidation):
    pass


def test_full_clean():
    msg = "dummy error"

    with pytest.raises(ValidationError) as err:
        DummyModel(ValidationError(msg)).save()

    assert msg in str(err)
