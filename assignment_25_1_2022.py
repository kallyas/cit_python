import requests

# 25/1/2022 assignment

# 1. We have a report on the number of flu vaccinations in a class of 40 people.
# It has the following numbers: never:8  once: 10 twice: 4 Threetimes:6
# What is the mean number of the times those people have been vaccinated?

def mean_vaccination():
    never = 8
    once = 10
    twice = 4
    threetimes = 6
    total = never + once + twice + threetimes
    mean = total / 4
    print("The mean number of the times those people have been vaccinated is:", mean)

mean_vaccination()

# 2. Create a store class that allow customers purchase items in your store
from store import Store, Product

items = []
try:
    products = requests.get('https://hub.dummyapis.com/products?noofRecords=10&idStarts=1001&currency=usd', timeout=10).json()

except:
    print("Error while fetching data")
    exit(-1)


for product in products:
    items.append(Product(product['name'],  int(float(product['price'][2:]))))

store = Store("CIT Store", items)

print(store.products)


# add a product to the store
print(store.add_products(Product("Coffee", 10)))
print(store.add_products(Product("Tea", 5)))

print(store.inflation(0.1))

print(store.print_products())

print(store.set_clearance(0.5))

print(store.print_products())

# sell a product
print(store.sell_product(Product('Tea')))

# remove a product
print(store.remove_products(Product('coffee')))


# 3. Create a polymorphism class funtion.

class Polymorphism():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def make_sound(self):
        print(f"{self.name} says hello")

    def move(self):
        print(f"{self.name} moves")


class Cat(Polymorphism):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def __str__(self):
        return f"{self.name} is {self.age} years old and has {self.fur_color} fur"

    def make_sound(self):
        print(f"{self.name} says meow")


class Dog(Polymorphism):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def __str__(self):
        return f"{self.name} is {self.age} years old and has {self.fur_color} fur"

    def make_sound(self):
        print(f"{self.name} says woof")


cat = Cat("Fluffy", 2, "white")
dog = Dog("Fido", 3, "brown")
print(cat)
print(dog)
cat.make_sound()
dog.make_sound()


"""
1.We have a report on the number of flu vaccinations in a class of 40 people.
It has the following numbers: never:10  once: 15 twice: 7 Threetimes:8
What is the mean number of the times those people have been vaccinated?

"""

number_of_people = 40
number_of_never = 10
number_of_once = 15
number_of_twice = 7
number_of_threetimes = 8

sum_vaccinated = number_of_once + number_of_twice + number_of_threetimes

mean_vaccinated = sum_vaccinated / number_of_people
print(f"The mean number of the times those people have been vaccinated is: {mean_vaccinated}")