from enum import Enum
from project_template.datamodels import common_utils


class RealEstateType(common_utils.IterableEnum):
    AGRICULTURAL = "Agricol"
    FOREST = "Forestier"
    URBAN = "Intravilan"
    LAKE = "Lucia de apa"
    OTHER = "Alte categorii"

    @classmethod
    def return_as_iterable(cls):
        return common_utils.return_enum_as_iterable(cls)
