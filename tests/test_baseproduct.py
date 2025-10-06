from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_initialization():
    """Тестируем инициализацию продукта."""
    product = Product("Смартфон", "Современный смартфон", 699.99, 50)
    assert product.name == "Смартфон"
    assert product.description == "Современный смартфон"
    assert product.price == 699.99
    assert product.quantity == 50


def test_product_str():
    """Тестируем строковое представление продукта."""
    product = Product("Смартфон", "Современный смартфон", 699.99, 50)
    expected_str = "Смартфон, 699.99 руб. Остаток: 50 шт."
    assert str(product) == expected_str


def test_product_addition():
    """Тестируем сложение двух продуктов."""
    product1 = Product("Смартфон", "Современный смартфон", 699.99, 50)
    product2 = Product("Ноутбук", "Мощный ноутбук", 999.99, 30)
    total_value = product1 + product2
    expected_value = (product1.price * product1.quantity) + (product2.price * product2.quantity)
    assert total_value == expected_value


def test_smartphone_initialization():
    """Тестируем инициализацию смартфона."""
    smartphone = Smartphone("Samsung Galaxy S23", "256GB, Серый цвет", 80000.0, 10, 95.5, "S23 Ultra", 256, "Серый")
    assert smartphone.name == "Samsung Galaxy S23"
    assert smartphone.price == 80000.0
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawngrass_initialization():
    """Тестируем инициализацию газонной травы."""
    lawn_grass = LawnGrass(
        "Газонная трава", "Качественная газонная трава", 1500.0, 20, "Россия", "7-14 дней", "Зеленый"
    )
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7-14 дней"
