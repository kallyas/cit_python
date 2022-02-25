"""
Author: Iden
Github: @kallyas
2022-25-02
"""

"""
1. You are given a program with two inputs: 
one as password and the second one as password repeat. 
Complete and call the given function to output "Correct" 
if password and repeat are equal, and output "Wrong", if they are not.
"""

def check_password(password: str, repeat_password) -> str:
    message = ""
    if password == repeat_password:
        message += "Correct"
    else:
        message += "Wrong"
    return message

print(check_password(input("Enter password: "), input("Repeat password: ")))
    
"""
2. You are making a phonebook. 
The contacts are stored in a dictionary, 
where the key is the name and the value is a list, 
representing the number and the email of the contact. 
You need to implement search: take the name of the contact 
as input and output the email. If the contact is not found, output "Not found".

"""

class PhoneBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, number, email):
        self.contacts[name] = [number, email]
    
    def search_contact(self, name):
        if name in self.contacts:
            return self.contacts[name][1]
        else:
            return "Not found"

    def display_contacts(self):
        for name, contact in self.contacts.items():
            print(name, contact[0], contact[1])


phonebook = PhoneBook()
phonebook.add_contact("John", "1234567", "john@gmail.com")
phonebook.add_contact("Mary", "7654321", "mary@gmail.com")

phonebook.display_contacts()
print(phonebook.search_contact("John"))
print(phonebook.search_contact("Ben"))


"""
3. Create a nesting list that prints out the color and the car brand.
"""

def create_car_nesting_list():
    return [[["color", "red"], ["brand", "BMW"]], [["color", "blue"], ["brand", "Audi"]], [["color", "green"], ["brand", "Mercedes"]]]

def print_list(car_list: list):
    for car in car_list:
        for key, value in car:
            print(f"{key}: {value}")

print_list(create_car_nesting_list())

"""
4. Create a game that the user plays the computer(CPU).
"""

class Game:
    def __init__(self, name: str, user_choice: str, computer_choice: str):
        self.name = name
        self.user_choice = user_choice
        self.computer_choice = computer_choice
    
    def play(self):
        if self.user_choice == self.computer_choice:
            return "Draw"
        elif self.user_choice == "rock" and self.computer_choice == "paper":
            return "Computer wins"
        elif self.user_choice == "paper" and self.computer_choice == "scissors":
            return "Computer wins"
        elif self.user_choice == "scissors" and self.computer_choice == "rock":
            return "User wins"
        elif self.user_choice == "rock" and self.computer_choice == "scissors":
            return "User wins"
        else:
            return "Invalid choice"


import random
game = Game("Rock, paper, scissors", input("Enter your choice: "), random.choice(["rock", "paper", "scissors"]))
print(game.play())


"""
5. Create a lists called daysoftheweek = ["Monday","Tuesday","Wednesday","Thursday","Friday"] you only could print out 3 days out that list.
"""

daysoftheweek = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
for day in daysoftheweek[0:3]:
    print(day)

"""
6. Bonus Question: Algorithm challenge: Create your own sorting algorithm.
"""
# break the list into two from the middle
# check if all the elements in the first half are 
# less than the elements in the second half
# if so swap them
# repeat until the list is sorted
# finally merge the lists

def merge_sort(list_to_sort: list):
    if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        mid = len(list_to_sort) // 2
        left_half = list_to_sort[:mid]
        right_half = list_to_sort[mid:]
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)
        return merge(left_half, right_half)


def merge(left_half: list, right_half: list):
    sorted_list = []
    while len(left_half) > 0 and len(right_half) > 0:
        if left_half[0] < right_half[0]:
            sorted_list.append(left_half[0])
            left_half.pop(0)
        else:
            sorted_list.append(right_half[0])
            right_half.pop(0)
    if len(left_half) > 0:
        sorted_list.extend(left_half)
    if len(right_half) > 0:
        sorted_list.extend(right_half)
    return sorted_list

print(merge_sort([6, 8, 1, 4, -4, -2]))



