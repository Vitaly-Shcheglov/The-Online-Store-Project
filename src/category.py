#
from src.product import Product  # Импорт класса Product


class Category:
    """Класс для представления категории продуктов."""

    # Атрибуты класса для хранения информации о количестве категорий и продуктов
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        """
        Инициализация экземпляра класса Category.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list): Список продуктов в категории (по умолчанию пустой список).
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []  # Инициализация списка продуктов

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Увеличиваем общий счетчик продуктов
        if products:
            Category.product_count += len(products)
            self.products.extend(products)  # Добавляем продукты в категорию

    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию и обновляет общий счетчик продуктов.

        Args:
            product (Product): Экземпляр продукта, который будет добавлен в категорию.
        """
        self.products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик продуктов
