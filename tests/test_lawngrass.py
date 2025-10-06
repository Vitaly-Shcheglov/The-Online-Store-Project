def test_lawn_grass_initialization(lawn_grass_example):
    """Функция тестирует инициализацию объекта LawnGrass."""
    assert lawn_grass_example.name == "Газонная трава"
    assert lawn_grass_example.description == "Качественная газонная трава"
    assert lawn_grass_example.price == 1500.0
    assert lawn_grass_example.quantity == 20
    assert lawn_grass_example.country == "Россия"
    assert lawn_grass_example.germination_period == "7-14 дней"
    assert lawn_grass_example.color == "Зеленый"


def test_lawn_grass_str(lawn_grass_example):
    """Функция тестирует строковое представление газонной травы."""
    expected_str = (
        "Газонная трава (Цвет: Зеленый, Страна: Россия, Срок прорастания: 7-14 дней), 1500.0 руб. Остаток: 20 шт."
    )
    assert str(lawn_grass_example) == expected_str


def test_lawn_grass_inheritance(lawn_grass_example):
    """Функция тестирует, что LawnGrass наследует свойства от Product."""
    assert lawn_grass_example.price == 1500.0
    assert lawn_grass_example.quantity == 20
