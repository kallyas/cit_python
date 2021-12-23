# Create a store using the class function. Product inventory,Cash register,etc. Use your creativity.
# class Store:

class Store:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def __str__(self):
        return f"{self.name} has {self.inventory} items in stock."

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def inventory_count(self):
        return len(self.inventory)

    def sell_item(self, item):
        self.inventory.remove(item)
        return f"{item} sold!"

    def restock_item(self, item, quantity):
        self.inventory.append(item)
        return f"{item} restocked!"

    def inventory_value(self):
        total_value = 0
        for item in self.inventory:
            total_value += item.price
        return total_value