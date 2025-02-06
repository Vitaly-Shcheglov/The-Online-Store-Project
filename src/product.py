class Product:
    """Класс для представления продукта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация экземпляра класса Product.

        Args:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта (может включать копейки).
            quantity (int): Количество продукта в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
