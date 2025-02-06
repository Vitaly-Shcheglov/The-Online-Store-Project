import json
import os
from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    """
    Читает JSON файл и возвращает данные в виде словаря.

    Args:
        path (str): Путь к файлу JSON.

    Returns:
        dict: Данные из файла JSON.
    """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list):
    """
    Создает объекты категорий и продуктов из данных JSON.

    Args:
        data (list): Данные, загруженные из JSON файла.

    Returns:
        List[Category]: Список объектов категорий с продуктами.
    """
    categories = []

    for category_data in data:
        # Создание экземпляра Category
        category = Category(name=category_data["name"], description=category_data["description"])

        # Создание списка продуктов для категории
        for product_data in category_data.get("products", []):
            product = Product(**product_data)  # Создание объекта Product
            category.add_product(product)  # Добавление продукта в категорию

        categories.append(category)  # Добавляем категорию в список

    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")  # Путь к файлу products.json
    categories_data = create_objects_from_json(raw_data)

    for category in categories_data:
        print(f"Категория: {category.name}, Описание: {category.description}")
        for product in category.products:
            print(f"  Продукт: {product.name}, Цена: {product.price}, Количество: {product.quantity}")
