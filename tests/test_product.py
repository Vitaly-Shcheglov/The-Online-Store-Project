import pytest

from src.product import Product


def test_product_initialization(product_example):
    """Функция тестирует инициализацию объекта Product."""
    assert product_example.name == "Смартфон"
    assert product_example.description == "Современный смартфон"
    assert product_example.price == 699.99
    assert product_example.quantity == 50


def test_product_price_setter(product_example):
    """Функция тестирует установку цены продукта."""
    product_example.price = 800.00
    assert product_example.price == 800.00


def test_product_price_setter_negative(product_example):
    """Функция тестирует установку отрицательной цены."""
    product_example.price = -100
    assert product_example.price == 699.99


def test_product_price_setter_zero(product_example):
    """Функция тестирует установку нулевой цены."""
    product_example.price = 0
    assert product_example.price == 699.99


def test_product_new_product(product_example):
    """Функция тестирует создание нового продукта с данными из словаря."""
    product_data = {
        "name": "Планшет",
        "description": "Современный планшет",
        "price": 499.99,
        "quantity": 25,
    }
    new_product = Product.new_product(product_data)
    assert new_product.name == "Планшет"
    assert new_product.description == "Современный планшет"
    assert new_product.price == 499.99
    assert new_product.quantity == 25


def test_product_new_product_existing(product_example):
    """Функция тестирует создание нового продукта, если продукт с таким же именем уже существует."""
    existing_products = [product_example]
    product_data = {
        "name": "Смартфон",
        "description": "Обновленный смартфон",
        "price": 750.00,
        "quantity": 30,
    }
    updated_product = Product.new_product(product_data, existing_products)
    assert updated_product.quantity == 80
    assert updated_product.price == 750.00


def test_product_new_product_existing_no_update(product_example):
    """Функция тестирует создание нового продукта без обновления, если цена ниже существующей."""
    existing_products = [product_example]
    product_data = {
        "name": "Смартфон",
        "description": "Обновленный смартфон",
        "price": 600.00,
        "quantity": 30,
    }
    updated_product = Product.new_product(product_data, existing_products)
    assert updated_product.quantity == 80
    assert updated_product.price == 699.99


def test_product_str(product_example):
    """Функция тестирует строковое представление продукта."""
    expected_str = "Смартфон, 699.99 руб. Остаток: 50 шт."
    assert str(product_example) == expected_str


def test_product_addition(product_example):
    """Функция тестирует сложение двух продуктов."""
    product2 = Product("Ноутбук", "Мощный ноутбук", 999.99, 30)
    total_value = product_example + product2
    expected_value = (product_example.price * product_example.quantity) + (product2.price * product2.quantity)
    assert total_value == expected_value


def test_product_initialization_zero_quantity():
    """Функция тестирует инициализацию объекта Product с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен."):
        Product("Смартфон", "Современный смартфон", 699.99, 0)
