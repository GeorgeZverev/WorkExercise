class Person:
    def __init__(self, fn: str, ln: str, ag: str, ss: str):
        self.__first_name = fn
        self.__last_name = ln
        self.__age = ag
        self.__social_security = ss

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, fn):
        self.__first_name = fn

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, ln):
        self.__last_name = ln

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, ag: str):
        self.__age = ag

    @property
    def social_security(self):
        return self.__social_security

    @social_security.setter
    def social_security(self, ss: str):
        self.__social_security = ss

    def key_value(self):
        str = f'First_name={self.__first_name}Last_name={self.__last_name}Age={self.__age}Social_security={self.__social_security}'
        return str

    def separator_semicolon(self):
        str = f'{self.__first_name};{self.__last_name};{self.__age};{self.__social_security}'
        return str

    def separator_space(self):
        data = []
        while len(self.__first_name) < 9:
            self.__first_name += ' '
        data.append(self.__first_name)
        while len(self.__last_name) < 10:
            self.__last_name += ' '
        data.append(self.__last_name)
        while len(self.__age) < 4:
            self.__age += ' '
        data.append(self.__age)
        while len(self.__social_security) < 12:
            self.__social_security += ' '
        data.append(self.__social_security)
        result = ''.join(data)
        return result


pr = Person('Mike', 'Wood', '32', '1321-234-2342')
pr.age = '45'
print(pr.key_value())
print(pr.separator_semicolon())
print(pr.separator_space())
