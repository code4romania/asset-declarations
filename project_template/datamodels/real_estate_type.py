from enum import Enum
from .common_utils import return_enum_as_iterable

class RealEstateType(Enum):
    AGRICULTURAL = "Agricol"
    FOREST = "Forestier"
    URBAN = "Intravilan"
    LAKE = "Lucia de apa"
    OTHER = "Alte categorii"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(RealEstateType)
