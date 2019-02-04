from enum import Enum
from datamodels import common_utils


class AccountType(Enum):
    CURRENT_ACCOUNT = (1, "Cont curent sau echivalente (inclusiv card)")
    BANK_DEPOSIT = (2, "Depozit bancar sau echivalente")
    INVESTMENT_FUNDS = (3, "Fonduri de investitii sau echivalente, inclusiv fonduri private de pensii sau alte sisteme "
                            "cu acumulare (se vor declara cele aferente anului fiscal anterior)")

    @staticmethod
    def return_as_iterable():
        enum_info_as_list = [member for name, member in AccountType.__members__.items()]
        values = [member.value for member in enum_info_as_list]

        return values
