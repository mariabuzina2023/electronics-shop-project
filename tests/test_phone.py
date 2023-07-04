import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone_():
    return Phone("Смартфон", 10000.0, 30, 1)


def test_number_of_sim(phone_):
    assert phone_.number_of_sim == 1
    phone_.number_of_sim = 0
    assert phone_.number_of_sim == 1


def test___radd__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + 10 == None


def test___str__(phone_):
    assert str(phone_) == "Смартфон"


def test___repr__(phone_):
    assert repr(phone_) == "Phone('Смартфон', 10000.0, 30, 1)"