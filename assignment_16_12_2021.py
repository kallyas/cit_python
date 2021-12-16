# create a cash system that has a sender, reciever and a robber.
# create a game using the class polymorphism.

class CashSystem:
    def __init__(self, sender, reciever, robber):
        self.sender = sender
        self.reciever = reciever
        self.robber = robber

    def send(self):
        self.sender.send()

    def recieve(self):
        self.reciever.recieve()

    def rob(self):
        self.robber.rob()


class Sender:
    def send(self):
        print("Sender send money")


class Reciever:
    def recieve(self):
        print("Reciever recieve money")


class Robber:
    def rob(self):
        print("Robber steal money")


cash = CashSystem(Sender(), Reciever(), Robber())
cash.send()
cash.recieve()
cash.rob()


class Game:
    def __init__(self, player):
        self.player = player

    def play(self):
        self.player.play()


class Player:
    def play(self):
        print("Player play")


class Player1(Player):
    def play(self):
        print("Player1 play")


class Player2(Player):
    def play(self):
        print("Player2 play")

player_1 = Player1()
player_2 = Player2()

player_1.play()
player_2.play()