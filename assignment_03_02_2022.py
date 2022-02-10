# 1. create a 2-D array and divide each array of both 2-D array
def create_2D_array(m, n):
    return [[i for i in range(m)] for j in range(n)]

def divide_2D_array(array, m, n):
    for i in range(m):
        for j in range(n):
            array[i][j] = i * j
    return array

arr = create_2D_array(3, 3)
# print(arr)
# print(divide_2D_array(arr, 3, 3))  

def create_country_with_capital():
    import json
    # open data.json file and read data
    countries = []
    with open("data.json", "r") as f:
        data = json.load(f)
        for country in data:
            countries.append({
                "name": country["name"],
                "capital": country["capital"]
            })
    return countries

# 2. create a game using if statements and user input
def capital_city_guess(countries: list):
    """
    using countries data, create a game
    """
    import random
    question = random.choice(countries)
    answer = input(f"what is the capital city of {question['name']}?")
    if answer.lower() == question["capital"].lower():
        print("you are correct, the capital city is", question["capital"])
    else:
        print("you are wrong")
        print(f"the capital city of {question['name']} is {question['capital']}\n")


# capital_city_guess(create_country_with_capital())

# 3. create a list, pop and replace an element in the list, then convert the list to a tuple
def create_list() -> list:
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pop_list(items: list) -> int:
    return items.pop()

def replace_list(items: list, value: int) -> list:
    items[0] = value
    return items

def to_tuple(items: list) -> tuple:
    return tuple(items)


# 4. create L pattern using letter L
def create_L_pattern():
    for i in range(5):
        print("L" * 8 if i == 4  else "L" )

# create_L_pattern()

# 5. create a while loop that prints your name 10 times
def print_name(name: str):
    i = 0
    while i < 10:
        print(name)
        i += 1

# print_name("Iden")

# 6. Create a program that prints out prime numbers using the while loop
def print_prime_numbers(n: int) -> list:
    prime_numbers = []
    i = 2
    while i < n:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
        i += 1
    return prime_numbers

# print(print_prime_numbers(100))

def main():
    # create a cli to run the programs
    import argparse
    parser = argparse.ArgumentParser(description="This is a cli to run the programs")
    parser.add_argument("-p", "--program", help="the program you want to run", type=str)
    parser.add_argument("-n", "--number", help="the number you want to run the program", type=int)
    args = parser.parse_args()
    if args.program == "prime":
        print(print_prime_numbers(args.number))
    elif args.program == "L":
        create_L_pattern()
    elif args.program == "name":
        print_name("Iden")
    elif args.program == "divide":
        print(divide_2D_array(arr, 3, 3))
    elif args.program == "capital":
        capital_city_guess(create_country_with_capital())
    elif args.program == "list" or args.program == "tuple" or args.program == "pop":
        items = create_list()
        print(items)
        popped_number = pop_list(items)
        print(replace_list(items, popped_number * 4))
        print(to_tuple(items))
    else:
        # print unrecognized program and show the help
        print(f"unrecognized program {args.program}")
        parser.print_help()



if __name__ == "__main__":
    main()