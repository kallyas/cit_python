# 1. create a for  loop that prints 8 rows of stars spaced going right

def star_rows():
    for i in range(1, 9):
        print('*' * i)


star_rows()

# create a for loop that prints 8 rows of stars spaced going left to right
def star_rows_left():
    for i in range(1, 9):
        print(' ' * (8 - i), '*' * i)


star_rows_left()    

# 2. create a for loop that prints up to 20 but skips 15

def skip_15():
    for i in range(1, 21):
        if i == 15:
            continue
        print(i)


# skip_15()

def print_pyramid():
    for i in range(1, 6):
        print(' ' * (5 - i), '*' * (2 * i - 1))

def pyramid_inverse():
    for i in range(1, 6):
        print(' ' * i, '*' * (2 * (5 - i) - 1))

pyramid_inverse()


print_pyramid()

# 3. create a dictionary and using a for loop print only values
def create_dict():
    fav_cars = {
        'ford': 'mustang',
        'chevy': 'camaro',
        'dodge': 'challenger',
        'jeep': 'wrangler'
    }
    # using a for loop print only values
    for value in fav_cars.values():
        print(value)


create_dict()