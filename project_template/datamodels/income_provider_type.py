from enum import Enum
from .common_utils import *

class IncomeProviderType(Enum):
    HOLDER = "Titular"
    SPOUSE = "Sot/sotie"
    KIDS = "Copii"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(IncomeProviderType)

