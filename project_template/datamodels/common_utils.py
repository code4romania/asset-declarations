from enum import Enum


class IterableEnum(Enum):

    @classmethod
    def return_as_iterable(cls):
        items = cls.__members__.items()
        member_values = [v for k, v in items]

        print(member_values)

        if all(isinstance(x, tuple) for x in member_values):
            enum_info_as_list = [member for name, member in cls.__members__.items()]
            # values = [(member.name, member.value) for member in enum_info_as_list]
            values = [member.value for member in enum_info_as_list]
        else:
            print(type(member_values[0]))
        return values

    #
    # @classmethod
    # def return_as_iterable(cls):
    #     return (1, 2, 3)
    #     items = cls.__members__.items()
    #     if all(isinstance(x, tuple) for x in items):
    #         # all enum members are tuples
    #         enum_info_as_list = [member for name, member in items]
    #         values = [member.value for member in enum_info_as_list]
    #     elif any(isinstance(x, str) for x in items):
    #         # the enum members are a mix of tuples and other types
    #         raise TypeError
    #     else:
    #         # all enum members are non-tuples
    #         enum_info_as_list = [member for name, member in cls.__members__.items()]
    #         values = [(member.name, member.value) for member in enum_info_as_list]
    #     return values


# Old stuff:

def return_enum_as_iterable(self):
    enum_info_as_list = [member for name, member in self.__members__.items()]
    values = [(member.name, member.value) for member in enum_info_as_list]

    return values


def return_as_ordered_iterable(self):
    enum_info_as_list = [member for name, member in self.__members__.items()]
    values = [member.value for member in enum_info_as_list]

    return values

