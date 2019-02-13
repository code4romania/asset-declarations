from enum import Enum
from .common_utils import return_enum_as_iterable

class AttainmentType(Enum):
    PURCHASE = "Cumparare/Contract Vanzare Cumparare"
    CONSTRUCTION = "Construire"
    DONATION = "Donatie"
    RETROCEDARE = "Retrocedare"
    RENT = "Inchiriere"
    INHERITANCE = "Mostenire"
    LEASING = "Leasing"
    OTHER = "Alt mod"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(AttainmentType)
