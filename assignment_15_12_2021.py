# Create a funtion that returns a string and a float.

def get_string_and_float():
    string = input("Enter a string: ")
    float_number = float(input("Enter a float: "))
    return string, float_number

string, float_number = get_string_and_float()
print(string, float_number)

# Create a nesting dictionary that prints keys and values.

def create_nesting_dictionary():
    count = int(input("How many nested dictionaries? : "))
    dictionary = {}
    # example: {'key1': {'key2': {'key3': 'value'}}}
    # input key count times 
    for i in range(count):
        key = input("Enter a key: ")
        # input value count times
        value = {}
        for j in range(int(input("How many nested values? : "))):
            value_key = input("Enter a nested key: ")
            value_value = input("Enter a nested value: ")
            value[value_key] = value_value
        dictionary[key] = value
    return dictionary

my_dictionary = create_nesting_dictionary()
print(my_dictionary)

#  Create a polymorphism class with 3 class with 3 roles.

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("I am an Animal")


class Dog(Animal):
    def speak(self):
        print("I am a Dog")

class Cat(Animal):
    def speak(self):
        print("I am a Cat")


cat = Cat("Cat")
dog = Dog("Dog")
animal = Animal("Animal")
cat.speak()
dog.speak()
animal.speak()


# Create a class function that the child class inherit from the parent class.

class Parent:
    def __init__(self, name, eye_color):
        self.name = name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name: " + self.name)
        print("Eye Color: " + self.eye_color)

class Child(Parent):
    def __init__(self, name, eye_color, number_of_toys):
        Parent.__init__(self, name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name: " + self.name)
        print("Eye Color: " + self.eye_color)
        print("Number of Toys: " + str(self.number_of_toys))

billy_cyrus = Parent("Billy Cyrus", "blue")
print(billy_cyrus.name)
print(billy_cyrus.eye_color)
billy_cyrus.show_info()

miley_cyrus = Child("Miley Cyrus", "blue", 5)
print(miley_cyrus.name)
print(miley_cyrus.eye_color)
print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()

# Create a class function that has a if statement that returns false.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        if self.age > 18:
            print("You are old enough to vote")
            return True
        else:
            print("Sorry, you are too young to vote")
            return False

p1 = Person("John", 36)
p1.myfunc()