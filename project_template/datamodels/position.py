from project_template.datamodels import common_utils


class Position(common_utils.IterableEnum):
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
