from project_template.datamodels import common_utils


class BuildingType(common_utils.IterableEnum):
    APARTMENT = (1, "Apartament")
    HOUSE = (2, "Casa de locuit")
    VACATION_HOUSE = (3, "Casa de vacanta")
    COMMERCIAL_SPACE = (4, "Spatii comerciale")
    OTHER = (5, "Alta categorie")
