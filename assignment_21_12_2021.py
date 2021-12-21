# 1. create a program using set data structures that prints out elements in both sets
fruits_set = {"apple", "banana", "cherry"}
vegetables_set = {"beetroot", "carrot", "cucumber"}

# use union to print out elements in both sets
print(fruits_set.union(vegetables_set))

# 2. create a factorial function that gives you the output 5040
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))

# 3. create a fibonacci series using user input
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(int(input("Enter a number: "))))

# 4. create a while loop that prints only odd numbers
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 5. create a class function that has a parent and 2 child classes
class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age


class Child2(Parent):
    def __init__(self, name, age, school):
        super().__init__(name)
        self.age = age
        self.school = school

    def get_age(self):
        return self.age

    def go_to_school(self, name):
            return self.name + " is going to " + self.school


child = Child("Joseph", 12)
child2 = Child2("John", 10, "Kampala school")
print(child.get_name())
print(child.get_age())
print(child2.get_name())
print(child2.get_age())
print(child2.go_to_school("John"))
