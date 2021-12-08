import numpy as np 
from scipy import stats 
import random
# 1. create a class called phonebook that prints out names with number.

class Phonebook:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def print_info(self):
        print(f'{self.name} {self.number}')


ph = Phonebook('John', '123-456-7890')
ph.print_info()

# 2 create a function that finds the median, mode, sum, and mean in a list.

def calc(list):
    median = np.median(list)
    mode = stats.mode(list)
    sum = np.sum(list)
    mean = np.mean(list)
    return median, mode, sum, mean

new_list = random.sample(range(1, 100), 15)
calc(new_list)

# 3create "2" 1-D array and multiply both of the arrays
def multiply(array1, array2):
    array3 = np.multiply(array1, array2)
    return array3

print(multiply(np.array([1,2,3]), np.array([4,5,6])))



# create an array that prints out odd numbers..
def odd_numbers(list):
    for i in list:
        if i % 2 == 1:
            print(i)

my_list = random.sample(range(1, 100), 10)
odd_numbers(my_list)


# create a tuple and convert it into a list and back to a tuple.
def convert(tup):
    list1 = list(tup)
    tuple1 = tuple(list1)
    return list1, tuple1

print(convert((1,2,3,4,5)))