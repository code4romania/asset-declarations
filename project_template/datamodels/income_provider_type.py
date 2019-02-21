from enum import Enum
from project_template.datamodels import common_utils


class IncomeProviderType(Enum):
    HOLDER = "Titular"
    SPOUSE = "Sot/sotie"
    KIDS = "Copii"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(IncomeProviderType)

