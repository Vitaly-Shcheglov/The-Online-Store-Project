import pytest

from src.utils import create_objects_from_json, read_json


def test_read_json(monkeypatch):
    """Тестирует функцию read_json."""

    mock_data = '{"name": "Электроника", "description": "Различные электронные устройства"}'

    def mock_open(*args, **kwargs):
        class MockFile:
            def __init__(self, data):
                self.data = data

            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                pass

            def read(self):
                return self.data

        return MockFile(mock_data)

    monkeypatch.setattr("builtins.open", mock_open)

    data = read_json("dummy_path")

    assert isinstance(data, dict)
    assert data["name"] == "Электроника"
    assert data["description"] == "Различные электронные устройства"


@pytest.fixture
def sample_json_data():
    """Фикстура для создания тестовых данных в формате JSON."""
    return [
        {
            "name": "Электроника",
            "description": "Различные электронные устройства",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Современный смартфон",
                    "price": 699.99,
                    "quantity": 50,
                },
                {
                    "name": "Ноутбук",
                    "description": "Мощный ноутбук",
                    "price": 999.99,
                    "quantity": 30,
                },
            ],
        },
        {
            "name": "Продукты",
            "description": "Еда и напитки",
            "products": [
                {
                    "name": "Яблоки",
                    "description": "Сочные яблоки",
                    "price": 1.50,
                    "quantity": 100,
                }
            ],
        },
    ]


def test_create_objects_from_json(sample_json_data):
    """Тестирует функцию create_objects_from_json."""
    categories = create_objects_from_json(sample_json_data)

    assert len(categories) == 2
    assert categories[0].name == "Электроника"
    assert categories[0].description == "Различные электронные устройства"
    assert len(categories[0].products) == 2

    assert categories[1].name == "Продукты"
    assert len(categories[1].products) == 1

    product = categories[0].products[0]
    assert product.name == "Смартфон"
    assert product.description == "Современный смартфон"
    assert product.price == 699.99
    assert product.quantity == 50
