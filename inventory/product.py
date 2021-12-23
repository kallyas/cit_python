# Product class:

class Product:
    def __init__(self, name, price, weight, brand, category):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.category = category

    def __str__(self):
        return f"{self.name} is a {self.weight} pound item from {self.brand}."

    def isValid(self):
        return self.price > 0 and self.weight > 0


        # product category class
class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} category"