from src.product import Product


class TestProduct(Product):
    """Класс для представления продукта с логированием."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    def log_creation(self):
        """Метод для логирования создания объекта."""
        print(
            f"Создан объект класса: {self.__class__.__name__} с параметрами: '{self.name}', '{self.description}',"
            f" {self.price}, {self.quantity}"
        )


def test_logging_on_creation(capfd):
    """Тестирует логирование при создании объекта."""
    product = TestProduct("Смартфон", "Современный смартфон", 699.99, 50)
    product.log_creation()

    captured = capfd.readouterr()

    expected_output = "Создан объект класса: TestProduct с параметрами: 'Смартфон', 'Современный смартфон', 699.99, 50"
    assert expected_output in captured.out


def test_logging_repr():
    """Тестирует строковое представление объекта."""
    product = TestProduct("Смартфон", "Современный смартфон", 699.99, 50)
    expected_repr = "<TestProduct(name='Смартфон', description='Современный смартфон', price=699.99, quantity=50)>"
    assert repr(product) == expected_repr


def test_product_initialization():
    """Тестирует инициализацию объекта Product."""
    product = TestProduct("Смартфон", "Современный смартфон", 699.99, 50)
    assert product.name == "Смартфон"
    assert product.description == "Современный смартфон"
    assert product.price == 699.99
    assert product.quantity == 50


def test_product_price_setter():
    """Тестирует установку цены продукта."""
    product = TestProduct("Смартфон", "Современный смартфон", 699.99, 50)
    product.price = 800.00
    assert product.price == 800.00


def test_product_price_setter_negative():
    """Тестирует установку отрицательной цены."""
    product = TestProduct("Смартфон", "Современный смартфон", 699.99, 50)
    product.price = -100
    assert product.price == 699.99


def test_product_price_setter_zero():
    """Тестирует установку нулевой цены."""
    product = TestProduct("Смартфон", "Современный смартфон", 699.99, 50)
    product.price = 0
    assert product.price == 699.99


def test_product_addition():
    """Тестирует сложение двух продуктов."""
    product1 = TestProduct("Смартфон", "Современный смартфон", 699.99, 50)
    product2 = TestProduct("Ноутбук", "Мощный ноутбук", 999.99, 30)
    total_value = product1 + product2
    expected_value = (product1.price * product1.quantity) + (product2.price * product2.quantity)
    assert total_value == expected_value
