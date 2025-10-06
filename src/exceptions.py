class ZeroQuantityError(Exception):
    """Исключение, которое вызывается при попытке добавить товар с нулевым количеством."""

    def __init__(self, product_name=None, message="Товар с нулевым количеством не может быть добавлен."):
        self.product_name = product_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        if self.product_name:
            return f"{self.message} (Товар: {self.product_name})"
        return self.message
