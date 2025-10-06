from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product


def test_category_initialization(category_example):
    """Функция тестирует инициализацию объекта Category."""
    assert category_example.name == "Электроника"
    assert category_example.description == "Различные электронные устройства"
    assert len(category_example.products) == 0


def test_product_count_in_category(category_example, product_example):
    """Функция тестирует подсчет количества продуктов в категории."""
    category_example.add_product(product_example)
    assert len(category_example.products) == 1
    assert Category.product_count == 1


def test_category_count():
    """Функция тестирует подсчет общего количества категорий."""
    initial_count = Category.category_count
    Category("Мебель", "Различная мебель")
    assert Category.category_count == initial_count + 1


def test_category_str(category_example):
    """Функция тестирует строковое представление категории."""
    expected_str = "Электроника, количество продуктов: 0 шт."
    assert str(category_example) == expected_str


def test_add_invalid_product(category_example):
    """Функция тестирует попытку добавления некорректного объекта в категорию."""
    with pytest.raises(TypeError):
        category_example.add_product("Некорректный продукт")


def test_middle_price_with_products(category_example, product_example):
    """Функция тестирует вычисление средней цены при наличии продуктов в категории."""

    with patch("builtins.input", return_value="y"):
        product_example.price = 100
        category_example.add_product(product_example)

        product_example2 = Product(name="Телевизор", description="Большой экран", price=200, quantity=30)
        category_example.add_product(product_example2)

    expected_average_price = (product_example.price + product_example2.price) / 2
    assert category_example.middle_price() == expected_average_price


def test_middle_price_no_products(category_example):
    """Функция тестирует вычисление средней цены, когда в категории нет продуктов."""
    assert category_example.middle_price() == 0
