# 1. Inside a funtion write a python program that goes through 3 conditional statements until it gets its final output.

def age_check():
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are not old enough to enter this site")
    elif age >= 18 and age < 21:
        print("You can enter but not drink")
    elif age >= 21:
        print("You can enter and drink")
    else:
        print("You are not old enough to enter this site")

age_check()

# 2. create a if statement using the (or)(and) operato
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "" or password == "":
        print("Please enter your username and password")
    elif username == "admin" and password == "admin":
        print("Welcome admin")
    else:
        print("Invalid username or password")

login_user()

# 3. Using the user input create a pyramid using the number 1.
def pyramid():
    height = int(input("Enter the height of the pyramid: "))
    for i in range(height):
        print(' ' * (height - i), '1' * (2 * i - 1))



pyramid()

# 4. Create a dictionary and add another item in your dictionary.
def dictionary():
    d = {"name": "John", "age": 30, "city": "New York"}
    d["nickname"] = "Jane"
    print(d)


dictionary()

# 5. Create a dictionary inside a dictionary and use the nesting loop to print your output.
def nested_dictionary():
    d = {"name": "John", "age": 30, "city": "New York"}
    d["nickname"] = "Jane"
    d["address"] = {"street": "Main", "number": "1000"}
    
    for key, value in d.items():
        print(key, value)


nested_dictionary()