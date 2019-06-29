from project_template.datamodels import common_utils


class Currency(common_utils.IterableEnum):
    EUR = "EUR"
    RON = "RON"
    USD = "USD"
    GBP = "GBP"
    CAD = "CAD"
    CHF = "CHF"
    ALTELE = "OTHER"
