from enum import Enum
from .common_utils import return_enum_as_iterable

class Currency(Enum):
    EUR = "EUR"
    RON = "RON"
    USD = "USD"
    GBP = "GBP"
    CAD = "CAD"
    CHF = "CHF"
    ALTELE = "OTHER"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(Currency)
