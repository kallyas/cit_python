"""
1.Create a function that transform an array from rows to columns.
2.Create an array,using the if statement find out if
the numbers of dimensions is correct.
3.Convert a list into an array and add two brackets to that new array.
4.Create two 2-d arrays and multiply each of them.
5.Create a right side triange pattern using the dollar sign'$'

"""

import numpy as np


def transform_array(array: np.array) -> np.array:
    """
    :param array: array to transform
    :return: array in columns
    """
    return array.reshape(len(array), 3)


def check_array(array: np.array) -> bool:
    """
    :param array: array to check
    :return: True if array is correct, False if not
    """
    return array.ndim == 2


def convert_list_to_array(list_to_convert: list) -> np.array:
    """
    :param list_to_convert: list to convert
    :return: array
    """
    return np.array(list_to_convert, ndmin=2)


def multiply_arrays(array1: np.array, array2: np.array) -> np.array:
    """
    :param array1: first array
    :param array2: second array
    :return: array1 * array2
    """
    return array1 * array2


def create_right_side_triangle(size: int) -> str:
    """
    :param size: size of triangle
    :return: right side triangle
    """
    while size > 0:
        print('$' * size)
        size -= 1
        

def main():
    """
    main function
    """
    arr_transform = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(transform_array(arr_transform))
    arr_check = np.array([[1, 2, 3], [4, 5, 6]])
    print(check_array(arr_check))
    list_to_convert = [1, 2, 3]
    print(convert_list_to_array(list_to_convert))
    array1 = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(multiply_arrays(array1, array2))
    print(create_right_side_triangle(5))


if __name__ == '__main__':
    main()
