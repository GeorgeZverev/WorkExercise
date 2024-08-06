import pytest
from src.oop_example import *


@pytest.fixture()
def param_person():
    person = Person('Mike', 'Wood', '45', '1321-234-2342')
    return person


def test_successful_launch(param_person):
    pr = param_person
    res = pr.__dict__
    assert res == {'_Person__first_name': 'Mike', '_Person__last_name': 'Wood', '_Person__age': '45', '_Person__social_security': '1321-234-2342'}


def test_key_value(param_person):
    pr = param_person
    res = pr.key_value()
    assert res == 'First_name=MikeLast_name=WoodAge=45Social_security=1321-234-2342'


def test_separator_semicolon(param_person):
    pr = param_person
    res = pr.separator_semicolon()
    assert res == 'Mike;Wood;45;1321-234-2342'


def test_separator_space(param_person):
    pr = param_person
    res = pr.separator_space()
    assert res == 'Mike     Wood      45  1321-234-2342'


def test_gettr_settr_first_name(param_person):
    pr = param_person
    res = pr.first_name
    assert res == "Mike"

    per = param_person
    per.first_name = 'John'
    assert per.first_name == 'John'


def test_gettr_settr_last_name(param_person):
    pr = param_person
    res = pr.last_name
    assert res == "Wood"

    per = param_person
    per.last_name = 'Kramer'
    assert per.last_name == 'Kramer'


def test_gettr_settr_age(param_person):
    pr = param_person
    res = pr.age
    assert res == '45'

    per = param_person
    per.age = '88'
    assert per.age == '88'


def test_gettr_settr_s_s(param_person):
    pr = param_person
    res = pr.social_security
    assert res == '1321-234-2342'

    per = param_person
    per.social_security = '4234-678-532'
    assert per.social_security == '4234-678-532'



