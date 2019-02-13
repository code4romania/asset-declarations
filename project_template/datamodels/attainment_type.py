from enum import Enum
from .common_utils import *

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
        return common_utils.return_enum_as_iterable(AttainmentType)
