"""
1. Create a program that shows a centralize payment system.
"""

class CentralizePaymentSystem:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({
            'amount': amount,
            'name': self.name,
            'balance': self.balance,
            'type': 'deposit',
            'id': len(self.transactions)
        })

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds')
        else:
            self.balance -= amount
            self.transactions.append({
                'amount': amount,
                'name': self.name,
                'balance': self.balance,
                'type': 'withdraw',
                'id': len(self.transactions)
            })

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def print_balance(self):
        print(f'Balance: {self.balance}')


"""
2. create a program that shows a decentralize payment system.
"""
import hashlib
import json
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


# DecentralizePayementSystem is a blockchain
class DecentralizePaymentSystem:
    def __init__(self):
        self.head = None
        

    def add_block(self, data):
        if self.head is None:
            self.head = Block(time.time(), data, 0)
        else:
            new_block = Block(time.time(), data, self.head.hash)
            self.head.next = new_block
            self.head = new_block

    def print_chain(self):
        current_block = self.head
        while current_block is not None:
            print(current_block.data)
            current_block = current_block.next


# create a decentralize payment system
blockchain = DecentralizePaymentSystem()


# create a centralize payment system
centralize_payment_system = CentralizePaymentSystem('John', 100, '12345')


"""
3. Show 1 & 2 in a graph
"""

import matplotlib.pyplot as plt


def plot_graph(centralize_payment_system, blockchain):
    x = []
    y = []
    for i in range(len(centralize_payment_system.transactions)):
        x.append(i)
        y.append(centralize_payment_system.transactions[i]['amount'])
    plt.plot(x, y)
    plt.show()

    x = []
    y = []
    for i in range(len(blockchain.transactions)):
        x.append(i)
        y.append(blockchain.transactions[i]['amount'])
    plt.plot(x, y)
    plt.show()


def main():
    centralize_payment_system.deposit(100)
    centralize_payment_system.deposit(200)
    centralize_payment_system.deposit(300)
    centralize_payment_system.withdraw(50)
    centralize_payment_system.withdraw(100)

    blockchain.add_block('first block')
    blockchain.add_block('second block')
    blockchain.add_block('third block')

    plot_graph(centralize_payment_system, blockchain)


if __name__ == '__main__':
    main()