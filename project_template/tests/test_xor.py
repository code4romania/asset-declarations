import pytest

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_template.utils import AutoCleanModelMixin, XORModelMixin


class DummyModel(AutoCleanModelMixin, XORModelMixin, models.Model):
    class Meta:
        abstract = True

    XOR_FIELDS = [{"commune": _("commune"), "city": _("city"),}]

    commune = ""
    city = ""


def test_xor():
    with pytest.raises(ValidationError) as err:
        DummyModel().save()

    assert "Foloseste doar unul din urmatoarele campuri: comuna, oras" in str(
        err
    )
