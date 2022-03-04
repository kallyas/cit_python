import numpy as np
"""
1. What method you use to add brackets to an array?
"""
# ndim

"""
2. What's the output of this code?x = np.arange(1,5,2)
"""
x = np.arange(1,5,2)
# output = [1, 3]

"""
3. Fill in the blank. Import numpy as _____.
"""
# np

"""
4. Create an array that outputs 6 rows and 6 columns. 
Then reshape it but it has to be more than 2 rows.
"""
def six_rows_six_columns():
    a = np.arange(1,37)
    a = a.reshape(6,6)
    return a

arr = six_rows_six_columns()
print(arr)

"""
5. Create a 2 d array with 6 columns and grab the 2 numbers in the second column.
"""
def two_d_array():
    a = np.arange(1,37)
    a = a.reshape(6,6)
    return a[:,1]

print(two_d_array())

"""
6. True or False? I could add boolean values in an array method?
"""
# True

"""
7. What is the out put of this code? y = np.([1,2,3,4]) print(y)
"""
# Syntax Error

"""
8. What's the output of this code? x = np.array([2,4,5,6]) y = np.array([12,14,16,18]) print(np.add(x,y))
"""
# [14 16 18 20]


"""
9. How do you find out the size of an array?
"""
# print(np.shape())

"""
10. Whats the output of this code? x = np.linspace(1,5) print(x)
"""
# [1. 5.]

"""
11. Create an array with 25 random numbers from 20 to 100. 
Find out how many numbers is greater than 55.
"""
def random_numbers_greater_than_55():
    a = np.random.randint(20,100,25)
    return np.sum(a > 55)

print(random_numbers_greater_than_55())

"""
12. Create a list called mph, the length of that list have to be 12. Using a function, 
find out the average mph in that list and also find the median value.
"""
def mph_list():
    a = np.random.randint(20,100,12)
    return np.mean(a), np.median(a)

mean, median = mph_list()
print(f"The mean is {mean} and the median is {median}")