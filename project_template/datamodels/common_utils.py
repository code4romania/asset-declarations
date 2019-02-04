def return_enum_as_iterable(self):
    enum_info_as_list = [member for name, member in self.__members__.items()]
    values = [(member.name, member.value) for member in enum_info_as_list]

    return values


def return_as_ordered_iterable(self):
    enum_info_as_list = [member for name, member in self.__members__.items()]
    values = [member.value for member in enum_info_as_list]

    return values

