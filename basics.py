# comment
"""
multline comment
"""

# float
# int
# string
# class
# dict
# tuple
# list

weight = 12.4
age = 12
name = "Iden"
my_books = {
    "name": "Book One",
    "age": 12,
    "likes": {
        "sports": "Foot ball"
    }
}

ages = (1, 2, 3)
ages2 = 1,2,3

my_list = list(ages)
# list -> []

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("class created!")

    def print_info(self):
        # return f"name is {self.name} and age is {self.age}"
        return "name is " + self.name + " and age is " + str(self.age)


person = Person("iden", 12)
print(person.print_info())

# dict methods
for keys in my_books.keys():
    print(keys)


for keys, values in my_books.items():
    print(f"{keys} => {values}")

# for number in my_list:
#     print(number)
count = 0

while count != len(my_list):
    print(my_list[count])
    count += 1

my_list.append(56)
print(my_list.count(2))


my_name = input("enter a name: ")

letter_count = 0
for letter in my_name:
    if "a" == letter:
        letter_count += 1
    else:
        continue
print(letter_count)