import pytest

from src.order import Order
from src.smartphone import Smartphone


@pytest.fixture
def smartphone_example():
    """Функция создает пример смартфона для тестирования."""
    return Smartphone("Samsung Galaxy S23", "256GB, Серый цвет", 80000.0, 10, 95.5, "S23 Ultra", 256, "Серый")


def test_order_initialization(smartphone_example):
    """Функция тестирует инициализацию объекта Order."""
    order = Order(product=smartphone_example, quantity=3)

    assert order.product.name == "Samsung Galaxy S23"
    assert order.quantity == 3
    assert order.total_cost == smartphone_example.price * order.quantity


def test_order_details(smartphone_example):
    """Функция тестирует метод details для заказа."""
    order = Order(product=smartphone_example, quantity=2)
    expected_details = (
        f"Заказ: {smartphone_example.name}, Количество: 2, Общая стоимость: {smartphone_example.price * 2} руб."
    )
    assert order.details() == expected_details


def test_order_str(smartphone_example):
    """Функция тестирует строковое представление объекта Order."""
    order = Order(product=smartphone_example, quantity=5)
    expected_str = (
        f"Заказ: {smartphone_example.name}, Количество: 5, Общая стоимость: {smartphone_example.price * 5} руб."
    )
    assert str(order) == expected_str
