# 1. .Create a star pattern that prints a pyramid using a while loop.
def star_pattern():
    n = int(input("Enter the height of the pyramid: "))
    i = 1
    while i <= n:
        print(' ' * (n - i), '*' * (2 * i - 1))
        i += 1


star_pattern()

# 2. Create a star pattern that prints a letter using a while loop.

def star_letter():
    length = 8
    i = 0
    while i < length:
        for col in range(length):
            if (col == 1 or ((i == 0 or i == 7 ) and (col > 1 and col < 7) ) or (col == 6 and i !=0 and i != 7)):
                print("*", end="")
            else:
                print(" ", end="" )
        print()
        i += 1


star_letter()

# 3. Create a dictionary that replace a key value pair with a new one.
def dictionary_replace():
    d = {"name": "John", "age": 30, "city": "New York"}
    print(d)
    d.pop("name")
    d["first_name"] = "Jane"
    print(d)


dictionary_replace()
