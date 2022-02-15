# Dice game playable over network.
import random
import socket


class Server:
    def __init__(self, port=8080):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', self.port))
        self.sock.listen()
        self.conn, self.addr = self.sock.accept()
        self.conn.settimeout(0.5)
        self.buffer = b''

    def recv(self):
        try:
            self.buffer += self.conn.recv(1024)
        except socket.timeout:
            pass
        return self.buffer

    def send(self, data):
        self.conn.send(data)

    def close(self):
        self.conn.close()
        self.sock.close()


class Client:
    def __init__(self, host, port=8080):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(0.5)
        self.buffer = b''

    def recv(self):
        try:
            self.buffer += self.sock.recv(1024)
        except socket.timeout:
            pass
        return self.buffer

    def send(self, data):
        self.sock.send(data)

    def close(self):
        self.sock.close()


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
    import argparse
    import sys
    parser = argparse.ArgumentParser(description='Dice game over network.')
    parser.add_argument('--host', default='localhost', help='Host to connect to.')
    parser.add_argument('--port', default=8080, type=int, help='Port to connect to.')
    parser.add_argument('--sides', default=6, type=int, help='Number of sides on the dice.')
    
    args = parser.parse_args()

    # player one is the first to connect
    player1 = Player('Iden')
    player2 = Player('Shawn')
    dice_game = DiceGame(player1, player2)

    server = Server(args.port)
    client = Client(args.host, args.port)

    # if no arguments are given, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    while True:
        server.recv()
        client.recv()

        if b'\n' in server.buffer:
            server_data = server.buffer.split(b'\n')
            server.buffer = server_data[1]
            client_data = client.buffer.split(b'\n')
            client.buffer = client_data[1]

            if server_data[0] == b'START':
                print('Starting game...')
                dice_game.play()
                server.send(b'END\n')
                client.send(b'END\n')
            elif server_data[0] == b'END':
                print('Game ended.')
                server.close()
                client.close()
                break
            else:
                print('Unknown command.')
                server.close()
                client.close()
                break
        else:
            server.buffer = b''
            client.buffer = b''


if __name__ == '__main__':
    main()
