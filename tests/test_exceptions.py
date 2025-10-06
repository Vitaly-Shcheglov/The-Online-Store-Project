import unittest


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


class TestZeroQuantityError(unittest.TestCase):

    def test_default_message(self):
        """Проверка, что сообщение по умолчанию правильно устанавливается."""
        with self.assertRaises(ZeroQuantityError) as context:
            raise ZeroQuantityError()
        self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен.")

    def test_custom_message(self):
        """Проверка, что пользовательское сообщение передается правильно."""
        custom_message = "Количество не может быть нулевым!"
        with self.assertRaises(ZeroQuantityError) as context:
            raise ZeroQuantityError(message=custom_message)
        self.assertEqual(str(context.exception), custom_message)

    def test_product_name_message(self):
        """Проверка, что имя товара добавляется к сообщению об ошибке."""
        product_name = "Яблоко"
        with self.assertRaises(ZeroQuantityError) as context:
            raise ZeroQuantityError(product_name=product_name)
        self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен. (Товар: Яблоко)")

    def test_custom_product_and_message(self):
        """Проверка, что как имя товара, так и пользовательское сообщение работают вместе."""
        product_name = "Груша"
        custom_message = "Количество недостаточно!"
        with self.assertRaises(ZeroQuantityError) as context:
            raise ZeroQuantityError(product_name=product_name, message=custom_message)
        self.assertEqual(str(context.exception), f"{custom_message} (Товар: {product_name})")
