from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Создает новый продукт на основе переданных данных."""
        pass

    @property
    @abstractmethod
    def price(self):
        """Геттер для получения цены продукта."""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float):
        """Сеттер для установки цены продукта с проверкой."""
        pass

    @abstractmethod
    def __str__(self):
        """Строковое представление продукта, должно быть реализовано в дочерних классах."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Магический метод сложения для подсчета полной стоимости."""
        pass
