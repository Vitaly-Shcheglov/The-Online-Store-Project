def test_smartphone_initialization(smartphone_example):
    """Функция тестирует инициализацию объекта Smartphone."""
    assert smartphone_example.name == "Samsung Galaxy S23"
    assert smartphone_example.description == "Современный смартфон"
    assert smartphone_example.price == 80000.0
    assert smartphone_example.quantity == 10
    assert smartphone_example.efficiency == 95.5
    assert smartphone_example.model == "Galaxy S23"
    assert smartphone_example.memory == 256
    assert smartphone_example.color == "Серый"


def test_smartphone_str(smartphone_example):
    """Функция тестирует строковое представление смартфона."""
    expected_str = "Samsung Galaxy S23 (Модель: Galaxy S23, Цвет: Серый, Память: 256 ГБ), 80000.0 руб. Остаток: 10 шт."
    assert str(smartphone_example) == expected_str


def test_smartphone_inheritance(smartphone_example):
    """Функция тестирует, что Smartphone наследует свойства от Product."""
    assert smartphone_example.price == 80000.0
    assert smartphone_example.quantity == 10
