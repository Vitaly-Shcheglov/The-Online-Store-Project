from src.product import Product


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            f"{self.name} (Модель: {self.model}, Цвет: {self.color}, "
            f"Память: {self.memory} ГБ), {self.price} руб. Остаток: {self.quantity} шт."
        )
