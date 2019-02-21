from enum import Enum
from project_template.datamodels import common_utils


class RealEstateType(Enum):
    AGRICULTURAL = "Agricol"
    FOREST = "Forestier"
    URBAN = "Intravilan"
    LAKE = "Lucia de apa"
    OTHER = "Alte categorii"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(RealEstateType)
