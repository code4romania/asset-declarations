from enum import Enum
from project_template.datamodels import common_utils

class DebtType(Enum):
    #valabila pentru situatia in care creditorul este persoana fizica (adaugat de Catalina)
    IMPRUMUT = "IMPRUMUT"
    DEBIT = "DEBIT"
    MORTGAGE = "IPOTECA"
    ISSUED_GARANTIES = "GARANTII EMISE"
    LEASING_ACQUIRED_GOODS = "BUNURI ACHIZIONATE LEASING"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(DebtType)
