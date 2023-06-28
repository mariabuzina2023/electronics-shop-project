"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import csv



def test_calculate_total_price():
    example = Item("Смартфон", 10000, 20)
    assert example.calculate_total_price() == 200000

def test_set_name():
    item = Item('Холодильник', 10000, 5)
    item1 = Item('утюг', 2000, 4)
    item.name = 'Холодильник'
    item1.name = 'утюг'
    assert item.name == 'Холодильни'
    assert item1.name == 'утюг'


def test_string_to_number():
    item = Item('Холодильник', 10000, 5)
    assert item.string_to_number('5') == 5


# def test_instantiate_from_csv():

def test_apply_discount():

    item = Item('Холодильник', 10000, 5)
    item.pay_rate = 1.0
    assert item.price == 10000


def test_repr():
    example = Item("Смартфон", 10000, 20)
    assert example.__repr__() == "Item('Смартфон', 10000, 20)"


def test_str():
    example = Item("Смартфон", 10000, 20)
    assert example.__str__() == 'Смартфон'








