#1. Create a list called ages and in a fuction find the average age in your list.

ages = [10, 20, 30, 40, 50]

def average_age(ages: list):
    sum_of_ages = 0
    for age in ages:
        sum_of_ages += age
    return sum_of_ages / len(ages)

print(average_age(ages))

# 2. You are given 2D matrix, which represents the number of people in a
# room, group by their eye color and gender. The first row represents
# the male gender,while the second row represents females.
# The colums are the eye colors, in the following order: brown,blue, 
# green,black.
# Create a program that needs to take eye color as input and output the 
# percentage of people with the eye color in the room

people = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0]
    ]


def percentage_of_people(people: list):
    total_people = 0
    for row in people:
        for element in row:
            total_people += element
    return total_people / (total_people + 1)


# 3. Create a class called bankaccount that has a deposit,withdraw,and statement

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def statement(self):
        return self.balance


account = BankAccount(100)
account.deposit(50)
account.withdraw(10)
account.statement()

# 4. Create a nesting dictionary that prints out all the items in your dictionary.

nesting_dict = {
    "Book One": {
        "title": "The Giver",
        "author": "Lois Lowry",
        "year": 1994
    },
    "Book Two": {
        "title": "Oliver Twist",
        "author": "Charles Dickens",
        "year": 1837
    },
    "Book Three": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951
    }
}

# print out all the items in your dictionary
for key, value in nesting_dict.items():
    print(key)
    for key, value in value.items():
        print(f"\t{key}: {value}")


# 5.Create a shopping cart program, the shopping cart is declared by a list 
# of prices,and you need to add the funtionality to apply a discount and output
# the total price.
# Take the discount percentage as the input,calculate and output the total price
# of the cart.

class ShoppingCart:
    def __init__(self, prices: list):
        self.prices = prices
        self.discount: float = 0.0

    def apply_discount(self, discount: float):
        self.discount = discount
        for price in self.prices:
            price -= price * discount
        return self.prices

    def total_price(self):
        total_price = 0
        for price in self.prices:
            total_price += price
        return total_price


cart = ShoppingCart([10, 20, 30])
cart.apply_discount(0.2)
cart.total_price()

