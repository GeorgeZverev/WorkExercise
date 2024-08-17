from attribute import Attribute


class Person:
    def __init__(self, fn: Attribute, ln: Attribute, ag: Attribute, ss: Attribute):
        self.__first_name = fn
        self.__last_name = ln
        self.__age = ag
        self.__social_security = ss

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, fn: Attribute):
        self.__first_name = fn

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, ln: Attribute):
        self.__last_name = ln

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, ag: Attribute):
        self.__age = ag

    @property
    def social_security(self):
        return self.__social_security

    @social_security.setter
    def social_security(self, ss: Attribute):
        self.__social_security = ss

    def name_value(self):
        str = f'First_name={self.__first_name.get_value}Last_name={self.__last_name.get_value}Age={self.__age.get_value}Social_security={self.__social_security.get_value}'
        return str

    def separator_semicolon(self):
        str = f'{self.__first_name.get_value};{self.__last_name.get_value};{self.__age.get_value};{self.__social_security.get_value}'
        return str

    # def separator_space(self):
    #     data = []
    #     while len(self.__first_name) < 9:
    #         self.__first_name += ' '
    #     data.append(self.__first_name)
    #     while len(self.__last_name) < 10:
    #         self.__last_name += ' '
    #     data.append(self.__last_name)
    #     while len(self.__age) < 4:
    #         self.__age += ' '
    #     data.append(self.__age)
    #     while len(self.__social_security) < 12:
    #         self.__social_security += ' '
    #     data.append(self.__social_security)
    #     result = ''.join(data)
    #     return result

    def separator_space(self) -> str:
        return (self.__first_name.get_value.ljust(self.__first_name.get_length, ' ') +
                self.__last_name.get_value.ljust(self.__last_name.get_length, ' ') +
                self.__age.get_value.ljust(self.__age.get_length, ' ') +
                self.__social_security.get_value.ljust(self.__social_security.get_length, ' '))


# pr = Person(Attribute('Mike', 9), Attribute('Wood', 10), Attribute('32', 4), Attribute('1321-234-2342', 11))
# print(pr.name_value())
# print(pr.separator_semicolon())
# print(pr.separator_space())
