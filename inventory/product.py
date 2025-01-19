from typing import Union

class Product:
    def __init__(self, name: str, price: float, weight: float, brand: str, category: 'Category'):
        """
        Initializes a new Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            weight (float): The weight of the product in pounds.
            brand (str): The brand of the product.
            category (Category): The category of the product.
        """
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.category = category

    def __str__(self) -> str:
        """
        Returns a string representation of the product.

        Returns:
            str: A string describing the product.
        """
        return f"{self.name} is a {self.weight} pound item from {self.brand}."

    def is_valid(self) -> bool:
        """
        Checks if the product is valid based on its price and weight.

        Returns:
            bool: True if the product has a positive price and weight, False otherwise.
        """
        return self.price > 0 and self.weight > 0


class Category:
    def __init__(self, name: str):
        """
        Initializes a new Category instance.

        Args:
            name (str): The name of the category.
        """
        self.name = name

    def __str__(self) -> str:
        """
        Returns a string representation of the category.

        Returns:
            str: A string describing the category.
        """
        return f"{self.name} category"
