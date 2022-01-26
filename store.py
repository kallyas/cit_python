# store class

from math import prod


class Store:
    def __init__(self, name, products):
        self.products = products
        self.name = name

    def __repr__(self):
        return f"Store({self.name}, {self.products})"

    def add_products(self, product):
        self.products.append(product)
        return f"{product['name']} added to {self.name}'s inventory"

    def remove_products(self, product):
        self.products.remove(product)
        return f"{product['name']} has been removed from {self.name}'s inventory"

    def stock_count(self):
        return len(self.products)

    def sell_product(self, product):
        self.products.remove(product)
        return f"{product['name']} has been sold!"

    def inflation(self, percent_increase):
        self.update_price(percent_increase, False)

    def set_clearance(self, percent_discount):
        self.update_price(percent_discount, True)

    def update_price(self, percent_increase, is_clearance):
        for product in self.products:
            if is_clearance:
                product['price'] = product['price'] * (1 - percent_increase)
            else:
                product['price'] = product['price'] * (1 + percent_increase)

# Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name}, {self.price})"

    def __str__(self):
        return self.name, self.price
        

    def update_price(self, percent_discount, is_clearance):
        if is_clearance:
            self.price = self.price - (self.price * percent_discount)
        else:
            self.price = self.price + (self.price * percent_discount)


        


        