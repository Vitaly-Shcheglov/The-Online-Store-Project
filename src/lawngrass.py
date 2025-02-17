from src.product import Product


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            f"{self.name} (Цвет: {self.color}, Страна: {self.country},"
            f" Срок прорастания: {self.germination_period}), {self.price} руб. Остаток: {self.quantity} шт."
        )
