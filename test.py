import numpy as np
import statistics

lst = [20,22,50,35,66,78,99,22] 

mean = np.mean(lst)
print(mean)

arr = np.arange(100,160,60) 
print(arr)

# Track = [4.1,5.1,4.5,4.9,5.6,7.5,8.5,] Find the mode value in this list using a function. *
Track = [4.1,5.1,4.5,4.9,5.6,7.5,8.5] 

def mode(Track):
    mode = max(set(Track), key=Track.count)
    return mode

print(mode(Track))

md = statistics.mode(Track)
print(md)

# What is the output for this code? print(2**3**3) *
print(2**3**3)

# Create a while loop that keeps adding the amount of grapes in hand 20 times. *
grapes = 0
while grapes < 20:
    grapes += 1
print(grapes)

# create a nesting list that prints out colors and cars. *
cars = [['red', 'green', 'blue'], ['toyota', 'ford', 'honda']]
for i in cars:
    for j in i:
        print(j)

# Using the magic method in a class function, print out 6 and 10. 
class MyClass:
    def __init__(self, num):
        self.num = num
    def __join__(self, other):
        return str(self.num) + ' ' + str(other.num)


x = MyClass(6)
y = x.__join__(MyClass(10))
print(y)

# ("Dave", "Jamie", "Jill", "Brenda") Which answer prints out Jamie? Pick Two.

tup = ("Dave", "Jamie", "Jill", "Brenda")
print(tup[1])

# Create a function that gives you a output of 2022
def year():
    return 2022

print(year())

# What is the output of this code? print(7 == 7) *
print(7 == 7)

# Create a dictionary that only prints out the values. 
d = {'k1': 1, 'k2': 2, 'k3': 3}
for i in d.values():
    print(i)

# What's the output of this code? Print(20 + 10 ** 2) 
print(20 + 10 ** 2)

# Create a 5 Dimensional array.
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

# Create a class function that inherits from the child class.
class Parent:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def print_age(self):
        print(self.age)

class GrandChild(Child):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city

    def print_city(self):
        print(self.city)
    
# Create a forloop that prints 1,3,5,7 as a output.
for i in range(1,8,2):
    print(i)

# Create a function that prints out "I Love Python" *
def love():
    print("I Love Python")