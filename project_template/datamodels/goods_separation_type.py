from enum import Enum
from .common_utils import *

class GoodsSeparationType(Enum):
    SELL = "Vanzare"
    SEPARATION = "Partaj"
    DONATION = "Donatie"
    ARBITRATION = "Executare"
    OTHER = "Alta forma"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(GoodsSeparationType)
