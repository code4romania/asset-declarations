from enum import Enum
from datamodels import common_utils


class EstrangedGoodsType(Enum):
    APARTMENT = "Apartament"
    HOUSE = "Casa de locuit"
    VACATION_HOUSE = "Casa de vacanta"
    COMMERCIAL_SPACE = "Spatii comerciale"
    AUTOVEHICLE = "Autovehicule/Autoturisme"
    TRACTOR = "Tractor"
    AGRICULTURAL_VEHICLE = "Masini agricole"
    BOATS = "Salupe"
    YACHTS = "Iahturi"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(EstrangedGoodsType)
