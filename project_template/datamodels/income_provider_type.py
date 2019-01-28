from enum import Enum
from datamodels import common_utils


class IncomeProviderType(Enum):
    HOLDER = "Titular"
    SPOUSE = "Sot/sotie"
    KIDS = "Copii"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(IncomeProviderType)

