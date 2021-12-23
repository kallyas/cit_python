# payement system for inventory
# This system handles the payment of the store.
# This system issues receipts for the store. and gives balance if needed.

class Payement:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name} has ${self.balance}."

    def pay(self, amount):
        self.balance -= amount
        return f"{self.name} paid ${amount}."

    def give_change(self, amount):
        self.balance += amount
        return f"{self.name} gave ${amount} back."

    def check_balance(self):
        return f"{self.name} has ${self.balance}."
