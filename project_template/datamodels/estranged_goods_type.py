from project_template.datamodels import common_utils


class EstrangedGoodsType(common_utils.IterableEnum):
    APARTMENT = "Apartament"
    HOUSE = "Casa de locuit"
    VACATION_HOUSE = "Casa de vacanta"
    COMMERCIAL_SPACE = "Spatii comerciale"
    AUTOVEHICLE = "Autovehicule/Autoturisme"
    TRACTOR = "Tractor"
    AGRICULTURAL_VEHICLE = "Masini agricole"
    BOATS = "Salupe"
    YACHTS = "Iahturi"
