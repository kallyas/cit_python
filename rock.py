# create a game using if condition statements
import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors? ").lower()

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print(f"You win! you chose {player} and computer chose {computer}")
    elif player == "rock" and computer == "paper":
        print(f"You lose! you chose {player} and computer chose {computer}")
    elif player == "paper" and computer == "rock":
        print(f"You win! you chose {player} and computer chose {computer}")
    elif player == "paper" and computer == "scissors":
        print(f"You lose! you chose {player} and computer chose {computer}")
    elif player == "scissors" and computer == "paper":
        print(f"You win! you chose {player} and computer chose {computer}")
    elif player == "scissors" and computer == "rock":
        print(f"You lose! you chose {player} and computer chose {computer}")
    else:
        print("Something went wrong!")

    play_again = input("Would you like to play again? (y/n) ").lower()
    if play_again == "n":
        break
    else:
        print("\n")
        continue


print("Thanks for playing!")

# create a python pyramid object using multiple numbers

multiples_of_two = [i for i in range(0, 21, 2)]
print(multiples_of_two)

def pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1) + f"{multiples_of_two[i]}" * (2 * i - 1))


pyramid(5)

