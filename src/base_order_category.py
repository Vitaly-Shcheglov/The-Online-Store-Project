from abc import ABC, abstractmethod


class BaseOrderCategory(ABC):
    """Абстрактный базовый класс для категорий и заказов."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def details(self):
        """Метод для получения деталей, должен быть реализован в дочерних классах."""
        pass
