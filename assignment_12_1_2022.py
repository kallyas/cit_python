# 1. create an upside down pyramid using stars

def upside_down_pyramid(rows):
    for i in range(1, rows):
       
        print(' ' * i, '*' * (2 * (rows - 1 - i) - 1))


upside_down_pyramid(5)

# 2. create a letter pattern using stars

def print_pattern(n):
    # Outer for loop for number of rows
    for row in range(n):

        # Inner for loop columns
        for column in range(n):

            # prints first and last and middle row
            if ((row == 0 or row == n - 1 or row == n // 2) or column == 0):
                    # prints first column
                    
                print("*", end="")
            else:
                print(" ", end="")
        print()


size = int(input("Enter size: \t"))

if size < 8:
    print("Enter a size greater than 8")
else:
    print_pattern(size)

# create a right side triangle using stars
def right_side_triangle(rows):
    for i in range(1, rows):
        print(' ' * (rows - i), '*' * i)

right_side_triangle(5)

# using list comprehension, print even numbers
def even_numbers(n):
    even_nums = [i for i in range(n) if i % 2 == 0]
    for num in even_nums:
        print(num)

even_numbers(int(input("Enter a number: \t")))

# using a lambda function, print 2022
lambda_function = lambda: print(2022)
lambda_function()