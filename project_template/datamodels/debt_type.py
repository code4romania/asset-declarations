from enum import Enum


class DebtType(Enum):
    #valabila pentru situatia in care creditorul este persoana fizica (adaugat de Catalina)
    IMPRUMUT = "IMPRUMUT"
    DEBIT = "DEBIT"
    MORTGAGE = "IPOTECA"
    ISSUED_GARANTIES = "GARANTII EMISE"
    LEASING_ACQUIRED_GOODS = "BUNURI ACHIZIONATE LEASING"
