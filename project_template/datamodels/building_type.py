from enum import Enum


class BuildingType(Enum):
    APARTMENT = (1, "Apartament")
    HOUSE = (2, "Casa de locuit")
    VACATION_HOUSE = (3, "Casa de vacanta")
    COMMERCIAL_SPACE = (4, "Spatii comerciale")
    OTHER = (5, "Alta categorie")

    @staticmethod
    def return_as_iterable():
        enum_info_as_list = [member for name, member in BuildingType.__members__.items()]
        values = [member.value for member in enum_info_as_list]

        return values
