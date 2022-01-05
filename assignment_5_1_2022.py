# 1.Write a program to take a number as input, and output a list of all the numbers
# below that number, that are a multiple of both, 3 and 5. 
# use list comprehension

def list_of_multiples(number):
    return [i for i in range(number) if i % 3 == 0 and i % 5 == 0]

multiples = list_of_multiples(int(input("Enter a range number: ")))
print("============= MULTIPLES =============")
print(multiples)

# 2. Create a nesting list, use user input

def nesting_list(n):
    list_of_numbers = [[ i for i in range(1, n, 2)] for x in range(n)]
    return list_of_numbers

nested_list = nesting_list(int(input("Enter a range number: ")))
print("============= NESTING LIST ==============")
print(nested_list)

# 3. Using the list comprenhension, print only odd numbers.

def odd_numbers(list_of_numbers):
    return [i for i in list_of_numbers if i % 2 == 1]

odd_nums = odd_numbers([i for i in range(int(input("Enter a number: ")))])
print("============= ODD NUMBERS ==============")
print(odd_nums)

# 4. Create a 4-D list and grab two elements out of that list
def four_d_list(n):
    list_of_numbers = [[[[i, (i+1), (i+2)] for i in range(1, 10, 3)]] for x in range(n)]
    two_elements = list_of_numbers[0][0][0][0:-1]
    return list_of_numbers, two_elements


list_of_nums, els = four_d_list(int(input("Enter a range number: ")))
print("============= 4D LIST ==============")
print(list_of_nums)
print("============= TWO ELEMENTS FROM 4D LIST ==============")
print(els)

# 5. Create a program that merge 2 list together.
def merge_list(list_1, list_2):
    return list_1 + list_2

fruit = ["apple", "banana", "orange"]
vegetable = ["carrot", "tomato", "potato"]
mereged_list = merge_list(fruit, vegetable)
print("============= MERGED LIST ==============")
print(mereged_list)
    