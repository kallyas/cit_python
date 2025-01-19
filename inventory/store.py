from typing import List, Union


class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}: ${self.price:.2f}"


class Store:
    def __init__(self, name: str, inventory: List[Item]):
        """
        Initializes the Store with a name and inventory.

        Args:
            name (str): The name of the store.
            inventory (List[Item]): The list of items in the store's inventory.
        """
        self.name = name
        self.inventory = inventory

    def __str__(self) -> str:
        return f"{self.name} has {len(self.inventory)} items in stock."

    def add_item(self, item: Item) -> None:
        """
        Adds an item to the store's inventory.

        Args:
            item (Item): The item to add to the inventory.
        """
        self.inventory.append(item)

    def remove_item(self, item: Item) -> None:
        """
        Removes an item from the store's inventory.

        Args:
            item (Item): The item to remove from the inventory.
        """
        self.inventory.remove(item)

    def inventory_count(self) -> int:
        """
        Returns the number of items in the store's inventory.

        Returns:
            int: The number of items in the inventory.
        """
        return len(self.inventory)

    def sell_item(self, item: Item) -> str:
        """
        Sells an item from the store's inventory.

        Args:
            item (Item): The item to sell.

        Returns:
            str: A message indicating the item has been sold.
        """
        self.inventory.remove(item)
        return f"{item} sold!"

    def restock_item(self, item: Item, quantity: int) -> str:
        """
        Restocks an item in the store's inventory.

        Args:
            item (Item): The item to restock.
            quantity (int): The quantity to restock.

        Returns:
            str: A message indicating the item has been restocked.
        """
        for _ in range(quantity):
            self.inventory.append(item)
        return f"{item} restocked with quantity {quantity}!"

    def inventory_value(self) -> float:
        """
        Calculates the total value of the store's inventory.

        Returns:
            float: The total value of the inventory.
        """
        total_value = sum(item.price for item in self.inventory)
        return total_value
