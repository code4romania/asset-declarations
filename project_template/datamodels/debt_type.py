from project_template.datamodels import common_utils


class DebtType(common_utils.IterableEnum):
    # valabila pentru situatia in care creditorul este persoana fizica (adaugat de Catalina)
    IMPRUMUT = "IMPRUMUT"
    DEBIT = "DEBIT"
    MORTGAGE = "IPOTECA"
    ISSUED_GARANTIES = "GARANTII EMISE"
    LEASING_ACQUIRED_GOODS = "BUNURI ACHIZIONATE LEASING"
