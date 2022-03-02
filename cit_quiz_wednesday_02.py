"""
1. Create a 2-D array and slice out the second number in the second column
"""

import numpy as np

def slice_array(array):
    """
    Returns a number in the second column
    """
    return array[:, 1][1]

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(slice_array(array))

"""
2. Create a list of numbers and find out the median value in that list using
a function.
"""

def median_list(list):
    """
    Returns the median value of the list.
    """
    return np.median(list)

list_arr = [3, 6, 4, 3, 2, 6, 8, 9, 7]
print(median_list(list_arr))

"""
3. Create an array with 20 random numbers and find out how many numbers is
greater than,less than, or equal to 55.
"""

def greater_than_less_than_equal_55(array):
    """
    Returns the number (count) of elements greater than 55, less than 55 and equal to 55
    """
    greater_than_55 = np.count_nonzero([x for x in array if x > 55])
    less_than_55 = np.count_nonzero([x for x in array if x < 55])
    equal_55 = np.count_nonzero([x for x in array if x == 55])
    return greater_than_55, less_than_55, equal_55


import random

random_array = [x for x in random.sample(range(100), 20)]
print(random_array)

greater_than_55, less_than_55, equal_55 = greater_than_less_than_equal_55(random_array)
print(f"Greater than 55: {greater_than_55}")
print(f"Less than 55: {less_than_55}")
print(f"Equal to 55: {equal_55}")
