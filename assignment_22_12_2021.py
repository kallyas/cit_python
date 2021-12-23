# 1.Create nesting loop that loop through 2 sets.
set_one = {"Mercury", "Venus", "Jupiter", "Saturn", "Uranus", "Neptune"}
set_two = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"}

def loop_nesting(set_one, set_two):
    for i in set_one:
        for j in set_two:
            # if one of the sets has the same element, print it only once
            if i == j:
                print(i)
            else:
                print(j)


loop_nesting(set_one, set_two)

# 2. Create a store using the class function. Product inventory,Cash register,etc. Use your creativity.
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


class Product:
    def __init__(self, name, price, weight, brand):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand

    def __str__(self):
        return f"{self.name} is a {self.weight} pound item from {self.brand}."


class Food(Product):
    def __init__(self, name, price, weight, brand, flavor):
        super().__init__(name, price, weight, brand)
        self.flavor = flavor

    def __str__(self):
        return f"{self.name} is a {self.weight} pound item from {self.brand} and has a {self.flavor} flavor."


class Toy(Product):
    def __init__(self, name, price, weight, brand, color):
        super().__init__(name, price, weight, brand)
        self.color = color

    def __str__(self):
        return f"{self.name} is a {self.weight} pound item from {self.brand} and has a {self.color} color."


store = Store("Bobs", [])
store.add_item(Product("Candy", 1.50, "1 lb", "M&M"))
store.add_item(Product("Chips", 1.00, "1 lb", "Lays"))
print(store.inventory_count())

#4. Create a dictionary called School. And have the keys and values to be the activities.
School = {"Math": "Addition", "Science": "Biology", "English": "Writing", "History": "Reading"}

for key, value in School.items():
    print(f"{key} is {value}")

#5.  Create a nesting list that prints the days of the week and activities. Example: Monday: Rollerskating.
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
activities = ["Rollerskating", "Swimming", "Hiking", "Biking", "Skiing", "Snowboarding", "Rock Climbing"]


def nested_list(days_of_the_week, activities):
    for i in range(len(days_of_the_week)):
        print(f"{days_of_the_week[i]} is for {activities[i]}")


nested_list(days_of_the_week, activities)


