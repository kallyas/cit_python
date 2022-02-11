# 1. create a function using the else and elif statements to get your output
def country_capital():
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
    
        """
    using countries data, create a game
    """
    import random
    question = random.choice(countries)
    answer = input(f"what is the capital city of {question['name']}?")
    if answer.lower() == "":
        print(f"you did not enter anything, the capital city of {question['name']} is {question['capital']}")
    elif answer.lower() == question["capital"].lower():
        print("you are correct, the capital city is", question["capital"])
    else:
        print("you are wrong")
        print(f"the capital city of {question['name']} is {question['capital']}\n")

# 2. create a nesting dictionary
def create_nesting_dictionary():
    """
    create a nesting dictionary
    """
    return {
        "name": "John",
        "age": 30,
        "address": {
            "street": "Main Street",
            "city": "Boston",
            "state": "MA"
        }
    }

# 3. create a while loop that only prints out odd numbers
def print_odd_numbers():
    """
    create a while loop that only prints out odd numbers
    """
    i = 1
    while i < 10:
        if i % 2 == 0:
            i += 1
        else:
            print(i)
            i += 1

# 4. make a function that converts foot to inch
# 1 ft = 12 in
def convert_foot_to_inch(feet: int):
    """
    make a function that converts foot to inch
    """
    return feet * 12

# 5. create a list and find the length of the list
def create_list():
    """
    create a list and find the length of the list
    """
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="This is a program that calls functions")
    parser.add_argument("-f", "--function", help="the function to call")
    args = parser.parse_args()
    if args.function == "country_capital":
        country_capital()
    elif args.function == "create_nesting_dictionary":
       my_dict = create_nesting_dictionary()
       for key, value in my_dict.items():
           print(f"{key}: {value}")
    elif args.function == "print_odd_numbers":
        print_odd_numbers()
    elif args.function == "convert_foot_to_inch":
        print(convert_foot_to_inch(5))
    elif args.function == "create_list":
        print(len(create_list()))
    elif args.function == "":
        print("please enter a function")
    else:
        # if the user enters a function that does not exist, print unknown function if function is not empty
        if args.function != None:
            print(f"unknown function {args.function}")
        else:
            # print usage 
            parser.print_usage()



if __name__ == "__main__":
    main()