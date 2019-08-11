from project_template.datamodels import common_utils


class HolderRelationship(common_utils.IterableEnum):
    HOLDER = "TITULAR"
    SPOUSE = "SOT/SOTIE"
    CHILDREN = "COPII"
