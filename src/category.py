from src.product import Product


class Category:
    """Класс для представления категории продуктов."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        """Инициализация экземпляра класса Category."""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1

        if products:
            Category.product_count += len(products)
            self.__products.extend(products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию и обновляет общий счетчик продуктов."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product и его наследников.")

        if self.__products and not isinstance(self.__products[0], type(product)):
            raise TypeError(
                f"Нельзя добавлять продукты разных типов: {type(self.__products[0]).__name__}"
                f" и {type(product).__name__}"
            )

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для получения списка продуктов в категории."""
        return self.__products

    def formatted_products(self):
        """Метод для получения отформатированного списка продуктов."""
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
