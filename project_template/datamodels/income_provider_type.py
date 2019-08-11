from project_template.datamodels import common_utils


class IncomeProviderType(common_utils.IterableEnum):
    HOLDER = "Titular"
    SPOUSE = "Sot/sotie"
    KIDS = "Copii"
