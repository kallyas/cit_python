"""
1. Create a 2-D array and using a funtion print out the number of dimension of that array.
2. You need to make a program that counts the number of vowels in a given text. The vowels are
a,e,i,o,u.
Take a string as input and output the number of vowels.
3.Create a upside down pyamid object pattern using binary numbers "1,0".

"""
import numpy as np


def print_array_dimension(array: np.ndarray):
    print(f"The dimension of the array is {array.ndim}")

def create_two_d_array():
    array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    return array

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count


def create_pyramid_reverse(rows):
    for i in range(1, rows):
        print(' ' * i, '01 ' * (1 * (rows - i) - 2))


# lambda function that checks a vowel in a string
check_vowel = lambda x: x in ['a', 'e', 'i', 'o', 'u']

def check_vowels_v2(string):
    return sum(1 for char in string if check_vowel(char))


def main():
    print_array_dimension(create_two_d_array())
    input_string = input("Enter a string: ")
    print(f"The number of vowels in the string {input_string} is {count_vowels(input_string)}")
    create_pyramid_reverse(10)
    print(f"The number of vowels in the string {input_string} is {check_vowels_v2(input_string)}")


if __name__ == '__main__':
    main()