from project_template.datamodels import common_utils


class AttainmentType(common_utils.IterableEnum):
    PURCHASE = "Cumparare/Contract Vanzare Cumparare"
    CONSTRUCTION = "Construire"
    DONATION = "Donatie"
    RETROCEDARE = "Retrocedare"
    RENT = "Inchiriere"
    INHERITANCE = "Mostenire"
    LEASING = "Leasing"
    OTHER = "Alt mod"
