class LoggingMixin:
    """Миксин для логирования создания объектов и их представления."""

    def __init__(self, *args, **kwargs):
        """Печатает информацию о создании объекта."""
        class_name = self.__class__.__name__
        parameters = ", ".join(repr(arg) for arg in args) + ", " + ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        print(f"Создан объект класса: {class_name} с параметрами: {parameters}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """Строковое представление объекта для отладки."""
        class_name = self.__class__.__name__
        return (
            f"<{class_name}(name={self.name!r}, description={self.description!r},"
            f" price={self._Product__price!r}, quantity={self.quantity!r})>"
        )
