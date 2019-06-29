from project_template.datamodels import common_utils


class InvestmentType(common_utils.IterableEnum):
    VALUE_PAPERS = "HARTII DE VALOARE"
    SHARES = "ACTIUNI/PARTI SOCIALE"
    PERSONAL_LOANS = "IMPRUMUTURI ACORDATE IN NUME PERSONAL"
