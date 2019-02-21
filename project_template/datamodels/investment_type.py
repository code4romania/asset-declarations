from enum import Enum
from project_template.datamodels import common_utils


class InvestmentType(Enum):
    VALUE_PAPERS = "HARTII DE VALOARE"
    SHARES = "ACTIUNI/PARTI SOCIALE"
    PERSONAL_LOANS = "IMPRUMUTURI ACORDATE IN NUME PERSONAL"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(InvestmentType)