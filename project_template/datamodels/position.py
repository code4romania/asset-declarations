from enum import Enum

from project_template.datamodels import common_utils


class Position(Enum):
    GENERAL_SECRETARY = "Secretar General"
    DEPUTY = "Deputat"
    SENATOR = "Senator"
    MEMBER_OF_PARLIAMENT = "Parlamentar"
    PRIME_MINISTER = "Prim Ministru"
    VICE_PRIME_MINISTER = "Vice Prim Ministru"
    MINISTER = "Minister"
    DEPUTY_CHAMBER_PRESIDENT = "Presedinte Camera Deputatilor"
    SENATE_PRESIDENT = "Presedinte Senat"
    PRESIDENT = "Presedinte"
    COUNSELOR = "Consilier"
    STATE_SECRETARY = "Secretar de Stat"
    OTHER = "Alta Valoare"


    @staticmethod
    def return_as_iterable():
        return common_utils.return_enum_as_iterable(Position)

