from src.category import Category


def test_category_initialization(category_example):
    """Функция тестирует инициализацию объекта Category."""
    assert category_example.name == "Электроника"
    assert category_example.description == "Различные электронные устройства"
    assert len(category_example.products) == 0


def test_product_count_in_category(category_example, product_example):
    """Функция тестирует подсчет количества продуктов в категории."""
    category_example.add_product(product_example)
    assert len(category_example.products) == 1
    assert Category.product_count == 1


def test_category_count():
    """Функция тестирует подсчет общего количества категорий."""
    initial_count = Category.category_count
    Category("Мебель", "Различная мебель")
    assert Category.category_count == initial_count + 1
