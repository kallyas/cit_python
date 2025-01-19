# Payment system for inventory
# This system handles the payment of the store.
# This system issues receipts for the store and gives balance if needed.

class Payment:
    def __init__(self, name: str, balance: float):
        """
        Initializes a new Payment instance.

        Args:
            name (str): The name of the payer.
            balance (float): The current balance of the payer.
        """
        self.name = name
        self.balance = balance

    def __str__(self) -> str:
        """
        Returns a string representation of the Payment instance.

        Returns:
            str: A string describing the current balance of the payer.
        """
        return f"{self.name} has ${self.balance:.2f}."

    def pay(self, amount: float) -> str:
        """
        Deducts the specified amount from the balance.

        Args:
            amount (float): The amount to deduct from the balance.

        Returns:
            str: A message indicating the payment was successful.
        """
        self.balance -= amount
        return f"{self.name} paid ${amount:.2f}."

    def give_change(self, amount: float) -> str:
        """
        Adds the specified amount to the balance.

        Args:
            amount (float): The amount to add to the balance.

        Returns:
            str: A message indicating the change was given.
        """
        self.balance += amount
        return f"{self.name} gave ${amount:.2f} back."

    def check_balance(self) -> str:
        """
        Returns the current balance.

        Returns:
            str: A message indicating the current balance.
        """
        return f"{self.name} has ${self.balance:.2f}."
