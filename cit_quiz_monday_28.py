"""
1. Create a 6-D array and flatten it to 1-D array.
"""
import numpy as np

def flatten_6d_array(array):
    """
    Flatten a 6-D array to 1-D array.
    """
    return np.array(array).flatten()


# create 6D array using ndim and shape
array = np.random.randint(0, 10, size=(2, 3, 4, 5, 6, 7))

print(flatten_6d_array(array))
p = flatten_6d_array(array)
print(p.ndim)


"""
2. Create a whileloop that prints only even numbers in a range of 20
but skips 16.
"""
def print_even_skip_16():
    """
    Print only even numbers in a range of 20 but skips 16.
    """
    i = 0
    while i < 20:
        if i == 16:
            i += 1
        if i % 2 == 0:
            print(i)
        i += 1


print_even_skip_16()

"""
3. Steph Curry has scored [22,55,43,31,38] points in 5 games. Using a
function, find out his total points average in 5 games.
"""

def average_points_in_5_games(points):
    """
    Calculate the average of points in 5 games.
    """
    return sum(points) / len(points)


points = [22, 55, 43, 31, 38]
print(average_points_in_5_games(points))

"""
4. Create a list and convert it into a tuple.
"""

def convert_list_to_tuple(list):
    """
    Convert a list into a tuple.
    """
    return tuple(list)

my_list = [1, 2, 3, 4, 5]
print(convert_list_to_tuple(my_list))

"""
5. Create any sorting algorithm using matplotlib.(Use my resources if needed)
"""

# create and visualize quick sort algorithm using matplotlib
import matplotlib.pyplot as plt


def quick_sort(array):
    """
    Quick sort algorithm.
    """
    if len(array) <= 1:
        return array
    else:
        # pick the first element as pivot
        pivot = array[0]
        # create two sub arrays
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        #  add visualization using bar chart
        plt.bar(range(len(array)), array)
        plt.pause(0.01)
        plt.clf()
        
        # return the concatenation of the sub arrays
        return quick_sort(less) + [pivot] + quick_sort(greater)


array = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
print(quick_sort(array))
plt.ioff()
plt.gcf().show()



