from enum import Enum
from .common_utils import return_enum_as_iterable

class GoodsSeparationType(Enum):
    SELL = "Vanzare"
    SEPARATION = "Partaj"
    DONATION = "Donatie"
    ARBITRATION = "Executare"
    OTHER = "Alta forma"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(GoodsSeparationType)
