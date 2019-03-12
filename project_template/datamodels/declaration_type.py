from enum import Enum
from project_template.datamodels import common_utils

class DeclarationType(Enum):
    ASSET = "Declaratie de avere"
    INTEREST = "Declaratie de interes"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(DeclarationType)
