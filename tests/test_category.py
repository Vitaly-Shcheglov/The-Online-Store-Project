import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def category_example():
    """Создает пример категории для тестирования."""
    return Category(name="Электроника", description="Различные электронные устройства")


@pytest.fixture
def product_example():
    """Создает пример продукта для тестирования."""
    return Product(name="Смартфон", description="Современный смартфон", price=699.99, quantity=50)


def test_category_initialization(category_example):
    """Тестирует инициализацию объекта Category."""
    assert category_example.name == "Электроника"
    assert category_example.description == "Различные электронные устройства"
    assert len(category_example.products) == 0  # Проверяем, что изначально нет продуктов


def test_product_count_in_category(category_example, product_example):
    """Тестирует подсчет количества продуктов в категории."""
    category_example.add_product(product_example)
    assert len(category_example.products) == 1  # Проверяем, что продукт добавлен
    assert Category.product_count == 1  # Проверяем общий счетчик продуктов


def test_category_count():
    """Тестирует подсчет общего количества категорий."""
    initial_count = Category.category_count
    Category("Мебель", "Различная мебель")
    assert Category.category_count == initial_count + 1  # Проверяем, что количество категорий увеличилось на 1
