import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product


@pytest.fixture
def product_example():
    """Функция создает пример продукта для тестирования."""
    return Product(
        name="Смартфон",
        description="Современный смартфон",
        price=699.99,
        quantity=50,
    )


@pytest.fixture
def category_example(product_example):
    """Функция создает пример категории для тестирования с одним продуктом."""
    return Category(name="Электроника", description="Различные электронные устройства", products=[product_example])


def test_category_iterator(category_example):
    """Тестирует функциональность итератора для категории."""
    iterator = CategoryIterator(category_example)

    products = list(iterator)

    assert len(products) == 2
    assert products[0].name == "Смартфон"


def test_category_iterator_empty():
    """Тестирует итератор для пустой категории."""
    empty_category = Category(name="Пустая категория", description="Нет продуктов")
    iterator = CategoryIterator(empty_category)

    products = list(iterator)
    assert len(products) == 0
