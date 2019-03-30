from enum import Enum

from project_template.datamodels import common_utils


class HolderRelationship(Enum):
    HOLDER = "TITULAR"
    SPOUSE = "SOT/SOTIE"
    CHILDREN = "COPII"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(HolderRelationship)
