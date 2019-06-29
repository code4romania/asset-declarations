from enum import Enum
from project_template.datamodels import common_utils


class HolderType(Enum):
    INSTITUTION = "Institutie"
    PERSON = "Persoana"

    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(HolderType)
