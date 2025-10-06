from src.base_order_category import BaseOrderCategory
from src.exceptions import ZeroQuantityError
from src.product import Product


class Order(BaseOrderCategory):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int):
        super().__init__(name=product.name, description=product.description)

        try:
            self.product = product
            self.quantity = quantity

            if self.quantity == 0:
                raise ZeroQuantityError()

            self.total_cost = self.calculate_total_cost()
            print(f"Товар '{self.product.name}' успешно добавлен в заказ.")

        except ZeroQuantityError as e:
            print(e)

        finally:
            print("Обработка добавления товара завершена.")

    def calculate_total_cost(self):
        """Вычисляет итоговую стоимость заказа."""
        return self.product.price * self.quantity

    def details(self):
        """Возвращает детали заказа."""
        return f"Заказ: {self.name}, Количество: {self.quantity}, Общая стоимость: {self.total_cost} руб."

    def __str__(self):
        """Строковое представление заказа."""
        return self.details()
