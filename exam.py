# To print out the text as shown below, what code should we execute? I love to take a ride in his sport's car!

print("I love to take a ride in his sport's car!")

# my_list = [1,3,5,7,9,11] Which of the following code will produce the same contents for my_list_2 as that stored in my_list?
my_list = [1,3,5,7,9,11]
my_list_2 = range(1,12,2)
print(my_list)
print(my_list_2)

# ("Dave", "Jamie", "Jill", "Brenda") Which answer prints out Jamie? Pick Two
names = ("Dave", "Jamie", "Jill", "Brenda")
print(names[1])
print(names[-3])
print(names[-4])

# Create a class function that inherits from the child class.
class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)
        print("Number of Toys - " + str(self.number_of_toys))

class GrandChild(Child):
    def __init__(self, last_name, eye_color, number_of_toys, number_of_cars):
        print("GrandChild Constructor Called")
        Child.__init__(self, last_name, eye_color, number_of_toys)
        self.number_of_cars = number_of_cars

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)
        print("Number of Toys - " + str(self.number_of_toys))
        print("Number of Cars - " + str(self.number_of_cars))

# Write a program to take a number as input, and output a list of all the numbers below that number, that are a multiple of both, 2 and 6.

def multiples_of_2_and_6(number):
   return [i for i in range(number) if i % 2 == 0 and i % 6 == 0]

multiples = multiples_of_2_and_6(int(input("Enter a number: ")))
print(multiples)

# We have a report on the number of flu vaccinations in a class of 20 people. It has the following numbers: never:5 once: 8 twice:4 Threetimes:3 What is the mean number of the times those people have been vaccinated?
class_len = 20
never = 5
once = 8
twice = 4
threetimes = 3

def mean_vaccinations(class_len, never, once, twice, threetimes):
    return ((never + once + twice + threetimes)) / class_len

print(mean_vaccinations(class_len, never, once, twice, threetimes))

# Create a program that prints out odd numbers using the while loop.

def odd_numbers():
    i = 1
    while i <= 100:
        if i % 2 == 1:
            print(i)
        i += 1

odd_numbers()

# create a file
f = open("test.txt", "w")


# phone number regex
import re

# UG phone format
# MTN: 077, 078, 076
# AIRTEL: 070, 075
# length: 10
def phone_number_validator(phone_number):
    airtel_regex = re.compile(r'^(070|075)')
    mtn_regex = re.compile(r'^(077|078|076)')
    if len(phone_number) == 10:
        if airtel_regex.search(phone_number) or mtn_regex.search(phone_number):
            return True
        else:
            return False
    else:
        return False
        