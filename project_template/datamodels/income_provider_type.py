from enum import Enum
from .common_utils import return_enum_as_iterable

class IncomeProviderType(Enum):
    HOLDER = "Titular"
    SPOUSE = "Sot/sotie"
    KIDS = "Copii"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(IncomeProviderType)

