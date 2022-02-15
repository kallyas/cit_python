"""
1.2 friends want to play a dice game, but have lost the dice.
Create a program to replace the dice. When the program is run, it should roll
the dice and output the result of each dice.

2.Create a while loop that prints your name 5 times in uppercase letters.

3.Create a pyramid pattern object using the number 1.

"""
import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class DiceGame:
    def __init__(self, dice=Dice()):
        self.dice = dice

    def play(self):
        return self.dice.roll()


def print_name(name):
    count = 0
    while count < 5:
        print(name.upper())
        count += 1

def print_pyramid(number):
    for i in range(1, number + 1):
        print(' ' * (number - 1 - i), '1' * (2 * i - 1))

    
def main():
    dice_game = DiceGame()
    print(f"The dice rolled {dice_game.play()}")
    print_name('Iden')
    print_pyramid(10)


if __name__ == '__main__':
    main()
