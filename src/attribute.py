class Attribute:
    __value = ""
    __length = 0

    def __init__(self, vl: str, ln: int):
        self.__value = vl
        self.__length = ln

    @property
    def get_value(self):
        return self.__value

    @property
    def get_length(self):
        return self.__length