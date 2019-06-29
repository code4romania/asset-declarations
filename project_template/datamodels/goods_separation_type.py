from project_template.datamodels import common_utils


class GoodsSeparationType(common_utils.IterableEnum):
    SELL = "Vanzare"
    SEPARATION = "Partaj"
    DONATION = "Donatie"
    ARBITRATION = "Executare"
    OTHER = "Alta forma"
