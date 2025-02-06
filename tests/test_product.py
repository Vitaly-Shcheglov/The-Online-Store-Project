def test_product_initialization(product_example):
    """Тестирует инициализацию объекта Product."""
    assert product_example.name == "Смартфон"
    assert product_example.description == "Современный смартфон"
    assert product_example.price == 699.99
    assert product_example.quantity == 50
