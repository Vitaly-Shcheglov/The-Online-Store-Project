import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция читает JSON файл и возвращает данные в виде словаря."""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list):
    """Функция создает объекты категорий и продуктов из данных JSON."""
    categories = []

    for category_data in data:

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
        )

        for product_data in category_data.get("products", []):
            product = Product(**product_data)
            category.add_product(product)

        categories.append(category)

    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    categories_data = create_objects_from_json(raw_data)

    for category in categories_data:
        print(f"Категория: {category.name}, Описание: {category.description}")
        for product in category.products:
            print(
                f"  Продукт: {product.name}, Цена: {product.price}, Количество: {product.quantity}"
            )
