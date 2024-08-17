import pytest
from person import Person
from attribute import Attribute


@pytest.fixture()
def param_person() -> Person:
    person = Person(Attribute('Mike', 9), Attribute('Wood', 10), Attribute('45', 4), Attribute('1321-234-2342', 11))
    return person


def test_successful_launch():
    pr = Person(Attribute('Mike', 9), Attribute('Wood', 10), Attribute('45', 4), Attribute('1321-234-2342', 11))
    res = (f'_Person__first_name: {pr.first_name.get_value}, _Person__last_name: {pr.last_name.get_value}, _Person__age: {pr.age.get_value},'
           f' _Person__social_security: {pr.social_security.get_value}')
    assert res == ('_Person__first_name:' 'Mike', '_Person__last_name:' 'Wood', '_Person__age:' '45', '_Person__social_security:' '1321-234-2342')


def test_key_value(param_person: Person):
    pr = param_person
    res = pr.name_value()
    assert res == 'First_name=MikeLast_name=WoodAge=45Social_security=1321-234-2342'


def test_separator_semicolon(param_person: Person):
    pr = param_person
    res = pr.separator_semicolon()
    assert res == 'Mike;Wood;45;1321-234-2342'


def test_separator_space(param_person: Person):
    pr = param_person
    res = pr.separator_space()
    assert res == 'Mike     Wood      45  1321-234-2342'


def test_gettr_settr_first_name(param_person: Person):
    pr = param_person
    res = pr.first_name.get_value
    assert res == "Mike"

    per = param_person
    per.first_name = 'John'
    assert per.first_name == 'John'


def test_gettr_settr_last_name(param_person: Person):
    pr = param_person
    res = pr.last_name.get_value
    assert res == "Wood"

    per = param_person
    per.last_name = 'Kramer'
    assert per.last_name == 'Kramer'


def test_gettr_settr_age(param_person: Person):
    pr = param_person
    res = pr.age.get_value
    assert res == '45'

    per = param_person
    per.age = '88'
    assert per.age == '88'


def test_gettr_settr_social_security(param_person: Person):
    pr = param_person
    res = pr.social_security.get_value
    assert res == '1321-234-2342'

    per = param_person
    per.social_security = '4234-678-532'
    assert per.social_security == '4234-678-532'



