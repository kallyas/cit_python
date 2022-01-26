# Product class
from typing import Union
class Product:
    def __init__(self, name: str, price: Union[int, float] = 0):
        self.product = {'name': name, 'price': price}

    def __repr__(self):
        return str(self.product)

    def get_name(self):
        return self.product['name']

    def get_price(self):
        return self.product['price']

    def update_price(self, percent_discount: float, is_clearance: bool):
        if is_clearance:
            self.product['price'] = self.product['price'] - (self.product['price'] * percent_discount)
        else:
            self.product['price'] = self.product['price'] + (self.product['price'] * percent_discount)



# store class
class Store:
    def __init__(self, name: str, products: list):
        self.products = products
        self.name = name

    def __repr__(self):
        return f"Store({self.name}, {self.products})"

    def print_products(self):
        for product in self.products:
            print(product.get_name(), product.get_price())

    def add_products(self, product: Product):
        self.products.append(product)
        return f"{str(product.get_name())} added to {self.name}'s inventory"

    def remove_products(self, product: Product):
        self.products = [p for p in self.products if p.get_name() != product.get_name()]
        return f"{str(product.get_name())} has been removed from {self.name}'s inventory"

    def stock_count(self):
        return len(self.products)

    def sell_product(self, product: Product):
        self.products = [p for p in self.products if p.get_name() != product.get_name()]
        return f"{product.get_name()} has been sold!"

    def inflation(self, percent_increase: float):
        for product in self.products:
            product.update_price(percent_increase, False)
        return f"Increased product price by {percent_increase}%"

    def set_clearance(self, percent_discount: float):
        for product in self.products:
            product.update_price(percent_discount, True)
        return f"Discounted products by {percent_discount}%"

