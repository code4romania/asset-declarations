from enum import Enum
from project_template.datamodels import common_utils


class GoodsSeparationType(Enum):
    SELL = "Vanzare"
    SEPARATION = "Partaj"
    DONATION = "Donatie"
    ARBITRATION = "Executare"
    OTHER = "Alta forma"

    @staticmethod
    def return_as_iterable():
        return return_enum_as_iterable(GoodsSeparationType)
