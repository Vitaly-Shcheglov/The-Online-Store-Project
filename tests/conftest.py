import pytest

from src.category import Category
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
def category_example():
    """Функция создает пример категории для тестирования."""
    return Category(
        name="Электроника", description="Различные электронные устройства"
    )
