"""
1. Create a list called fruits and show us which fruit has the 
most sales using matplotlib.
"""
import matplotlib.pyplot as plt
import numpy as np
import random

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_sales = [10, 101, 12, 31, 104, 105, 70]


def visualize_fruits_sales(fruits, fruits_sales):
    """
    Visualize fruits sales
    """
    # create a pie chart
    plt.pie(fruits_sales, labels=fruits, autopct='%1.1f%%',
            shadow=True, startangle=140)
    # draw circle
    plt.axis('equal')

    # show title
    plt.title("A Pie Chart of Fruits Sales")
    # show legend
    plt.legend()
    # show the plot
    plt.show()



visualize_fruits_sales(fruits, fruits_sales)

"""
2. Create 4-D array then reshape it.
"""

def reshape_4d_array(array):
    """
    Reshape 4-D array
    """
    return array.reshape(2, 2, 2)

array_4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])

print(reshape_4d_array(array_4d))

"""
3. Create a list of numbers and find out how many duplicate
values is in your list.
"""

def check_and_count_duplicate_values(list_of_numbers):
    """
    Check and count duplicate values
    """
    # create a dictionary
    duplicate_values = {}
    # loop through the list
    for number in list_of_numbers:
        # if the number is in the dictionary
        if number in duplicate_values:
            # increase the value by 1
            duplicate_values[number] += 1
        # if the number is not in the dictionary
        else:
            # add the number to the dictionary
            duplicate_values[number] = 1
    # return the dictionary
    return duplicate_values



list_with_duplicate_values = [45, 23, 2, 78, 2, 12, 10, 45, 45, 29]
print(check_and_count_duplicate_values(list_with_duplicate_values))


"""
4. Create 2 arrays and divide both of them.
"""

def divide_arrays(array_1, array_2):
    """
    Divide arrays
    """
    # create a list
    divided_array = []
    # loop through the first array
    for index in range(len(array_1)):
        # divide the first array with the second array
        divided_array.append(array_1[index] / array_2[index])
    # return the list
    return divided_array




array_1 = [1, 2, 3, 4, 5]
array_2 = [2, 4, 6, 8, 10]
print(divide_arrays(array_1, array_2))
