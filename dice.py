# Dice game playable by two players.
import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Player:
    def __init__(self, name, dice=Dice()):
        self.name = name
        self.dice = dice

    def roll(self):
        return self.dice.roll()


class DiceGame:
    def __init__(self, player1, player2, dice=Dice()):
        self.player1 = player1
        self.player2 = player2
        self.dice = dice

    def play(self):
        while True:
            player1_roll = self.player1.roll()
            player2_roll = self.player2.roll()
            if player1_roll > player2_roll:
                print(f"{self.player1.name} wins! with {player1_roll}")
                break
            elif player1_roll < player2_roll:
                print(f"{self.player2.name} wins! with {player2_roll}")
                break
            else:
                print(f"Tie! Both players rolled {player1_roll}")


def main():
    player1 = Player('Iden')
    player2 = Player('Shawn')
    dice_game = DiceGame(player1, player2)
    dice_game.play()


if __name__ == '__main__':
    main()