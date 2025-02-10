from src.product import Product


class Category:
    """Класс для представления категории продуктов."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        """Инициализация экземпляра класса Category."""
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1

        if products:
            Category.product_count += len(products)
            self.products.extend(products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию и обновляет общий счетчик продуктов."""
        self.products.append(product)
        Category.product_count += 1
