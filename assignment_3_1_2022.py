# 1. create a file and write what is your goals for this year

def create_file():
    goals = []
    # promt user to enter goals for this year, until user enter 'done'
    while True:
        goal = input("Enter your goals for this year and type done when finished: ")
        if goal == 'done':
            break
        goals.append(goal)
    # create a file and write goals to the file
    with open('goals.txt', 'w') as f:
        for goal in goals:
            f.write(goal + '\n')


create_file()

# 2. create a lambda function using 3 arguments
lambda_function = lambda x, y, z: x + y + z

print(lambda_function(1, 2, 3))

# 3. create a function that use user input.
def user_input():
    filename = input("Enter a filename: ")
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')


user_input()

# 4. create a while loop that prints 1-30  but skips 25
def skip_25():
    i = 1
    while i <= 30:
        if i == 25:
            i += 1
        print(i)
        i += 1


skip_25()

# 5. create a function that prints out random numbers. use two arguments
import random
def random_numbers(start, end):
        print(random.randint(start, end))

random_numbers(int(input("Enter a start number: ")), int(input("Enter an end number: ")))




        