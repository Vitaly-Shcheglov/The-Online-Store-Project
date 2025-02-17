import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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
    return Category(name="Электроника", description="Различные электронные устройства")


@pytest.fixture
def lawn_grass_example():
    """Функция создает пример газонной травы для тестирования."""
    return LawnGrass(
        name="Газонная трава",
        description="Качественная газонная трава",
        price=1500.0,
        quantity=20,
        country="Россия",
        germination_period="7-14 дней",
        color="Зеленый",
    )


@pytest.fixture
def smartphone_example():
    """Функция создает пример смартфона для тестирования."""
    return Smartphone(
        name="Samsung Galaxy S23",
        description="Современный смартфон",
        price=80000.0,
        quantity=10,
        efficiency=95.5,
        model="Galaxy S23",
        memory=256,
        color="Серый",
    )
