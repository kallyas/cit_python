# Write a function that takes a string and a letter as its 
# arguments and returns the count of the letter in string.
# Hint use the user input and the count method.

def count_letter(string, letter):
    # count = 0
    # for i in string:
    #     if i.lower() == letter.lower():
    #         count += 1
    # return count
    return string.lower().count(letter.lower())

string = input("Enter a string: ")
letter = input("Enter a letter: ")
print(f"The count of {letter} in {string} is {count_letter(string, letter)}")
# 2.  Create a list that prints all items in your list from uppercase to lowercase.
def uppercase_lowercase(list):
    for i in list:
        print(i.lower())

uppercase_lowercase(["A", "B", "C", "D"])

# 3.Create a while loop that prints odd numbers from 1 - 15 but skips 5
def odd_numbers():
    i = 1
    while i <= 15:
        if i == 5:
            i += 2
        else:
            print(i)
            i += 2

odd_numbers()

# 4. Create a tuple of items and convert it into a list.
def tuple_to_list(tup):
    return list(tup)

fruits = ("apple", "banana", "cherry")
print(tuple_to_list(fruits))

def upper_lower_case(list):
    lowercase = []
    for i in list:
        lowercase.append(i.lower())
    return lowercase

print(upper_lower_case(["JUICE", "APPLE", "BANANA", "CHERRY"]))