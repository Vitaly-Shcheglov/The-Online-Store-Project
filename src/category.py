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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

        else:
            raise TypeError

    @property
    def products(self):
        """Геттер для получения списка продуктов в категории."""
        return self.__products

    def formatted_products(self):
        """Метод для получения отформатированного списка продуктов."""
        return "\n".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
        )

    def middle_price(self):
        """Вызывает среднюю цену всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
