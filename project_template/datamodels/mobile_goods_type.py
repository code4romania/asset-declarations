from project_template.datamodels import common_utils


class MobileGoodsType(common_utils.IterableEnum):
    AUTOVEHICLE = "Autovehicule/Autoturisme"
    TRACTOR = "Tractor"
    AGRICULTURAL_VEHICLE = "Masini agricole"
    BOATS = "Salupe"
    YACHTS = "Iahturi"
    OTHER = "Altele"
