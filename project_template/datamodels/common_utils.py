from enum import Enum


class IterableEnum(Enum):
    """
    An Enum type which can return its members' values as an iterable
    """
    @classmethod
    def return_as_iterable(cls):
        member_values = [v.value for k, v in cls.__members__.items()]

        if all(isinstance(x, tuple) for x in member_values):
            # all Enum member values are tuples
            enum_info_as_list = [member for name, member in cls.__members__.items()]
            values = [member.value for member in enum_info_as_list]

        elif any(isinstance(x, tuple) for x in member_values):
            # the Enum member values are a mix of tuples and other types
            raise TypeError

        else:
            # all Enum member values are non-tuples
            enum_info_as_list = [member for name, member in cls.__members__.items()]
            values = [(member.name, member.value) for member in enum_info_as_list]

        return values
