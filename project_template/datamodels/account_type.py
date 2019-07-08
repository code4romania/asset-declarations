from project_template.datamodels import common_utils


class AccountType(common_utils.IterableEnum):
    CURRENT_ACCOUNT = (1, "Cont curent sau echivalente (inclusiv card)")
    BANK_DEPOSIT = (2, "Depozit bancar sau echivalente")
    INVESTMENT_FUNDS = (3, "Fonduri de investitii sau echivalente, inclusiv fonduri private de pensii sau alte sisteme "
                            "cu acumulare (se vor declara cele aferente anului fiscal anterior)")
