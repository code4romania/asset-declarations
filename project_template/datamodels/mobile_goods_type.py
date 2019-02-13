from enum import Enum

from .common_utils import *

class MobileGoodsType(Enum):
    AUTOVEHICLE = "Autovehicule/Autoturisme"
    TRACTOR = "Tractor"
    AGRICULTURAL_VEHICLE = "Masini agricole"
    BOATS = "Salupe"
    YACHTS = "Iahturi"
    OTHER = "Altele"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(MobileGoodsType)