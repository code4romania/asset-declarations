from enum import Enum
from project_template.datamodels import common_utils


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
