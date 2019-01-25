from enum import Enum
from datamodels import common_utils

class InvestmentType(Enum):
    VALUE_PAPERS = "HARTII DE VALOARE"
    SHARES = "ACTIUNI/PARTI SOCIALE"
    PERSONAL_LOANS = "IMPRUMUTURI ACORDATE IN NUME PERSONAL"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(InvestmentType)