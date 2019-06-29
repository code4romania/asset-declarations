from project_template.datamodels import common_utils


class RealEstateType(common_utils.IterableEnum):
    AGRICULTURAL = "Agricol"
    FOREST = "Forestier"
    URBAN = "Intravilan"
    LAKE = "Lucia de apa"
    OTHER = "Alte categorii"
