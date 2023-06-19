"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    example = Item("Смартфон", 10000, 20)
    assert example.calculate_total_price() == 200000


