"""
1. 50 percent of the class failed the exam,
create a list of student scores that scored
under a 70.
"""

def percent_failed(scores):
    """
    Returns the percentage of students that failed
    the exam.
    """
    return len([score for score in scores if score < 70]) / len(scores) * 100

scores = [100, 80, 90, 70, 60, 50, 40, 30, 20, 10]
print(percent_failed(scores))

"""
2. create a 6-D array and transform it to all rows
"""

import numpy as np
import random

# create a 6-D array of random numbers
array = np.array([[random.randint(0, 10) for _ in range(6)] for _ in range(6)])

def transform_array(array):
    """
    Returns a new array with all rows transformed.
    """
    return np.apply_along_axis(lambda x: x + 1, 0, array)


print(transform_array(array))

"""
3. create an 8-D array and reshape the array
"""

def reshape_array(array):
    """
    Returns a new reshaped array.
    """
    return array.reshape(2, 2, 2, 2, 2, 2)

# create 8-D array of random numbers
array = np.array([[random.randint(0, 10) for _ in range(8)] for _ in range(8)])

print(reshape_array(array))

"""
4. create a x and y array, multiply it and then reshape it to a new array
"""

x_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y_array = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

def multiply_and_reshape(x_array, y_array):
    """
    Returns a new array.
    """
    return (x_array * y_array).reshape(3, 3, 1)


print(multiply_and_reshape(x_array, y_array))