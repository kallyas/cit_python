"""
1. What is the protocol for btc?
"""
# BTC

"""
2. Name the 3 steps of a bitcoin transaction.
"""
# 1. Create a transaction
# 2. Sign the transaction
# 3. Send the transaction

"""
3. Which is a blockchain consensus algorithm?
"""
# Proof of Work

"""
4. What is BYZANTINE FAULT TOLERANCE?
"""
# is the property of a computer system that allows it to reach consensus regardless of the failure of some of its components.

"""
5. True of False? A decentralize network has an authority operating the network.
"""
# True

"""
6. What is the average block time for bitcoin?
"""
# 10 minutes

import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
import matplotlib.dates as mdates

"""
7. Create a program that displays the halving chart and turn that chart into a dataframe.
"""
def halving_chart():
    """
    Create a program that displays the halving chart and turn that chart into a dataframe.
    """
    # Create a list of dates
    date_list = []
    for i in range(0, 21):
        date_list.append(datetime.datetime.now() + datetime.timedelta(days=i))

    # Create a list of block sizes
    block_size_list = []
    for i in range(0, 21):
        block_size_list.append(2**i)

    # Create a dataframe
    df = pd.DataFrame({'Date': date_list, 'Block Size': block_size_list})

    # Plot the dataframe
    df.plot(x='Date', y='Block Size', kind='line')
    return df


halving_chart()

"""
8. The halving chart you created display the year and the bitcoin reward in 3 different graphs.
"""
def halving_chart_graphs():
    """
    The halving chart you created display the year and the bitcoin reward in 3 different graphs.
    """
    df = halving_chart()

    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    ax[0].plot(df['Date'], df['Block Size'])
    ax[0].set_title('Block Size')
    
    # bar graph
    ax[1].bar(df['Date'], df['Block Size'])
    ax[1].set_title('Block Size')

    # pie chart
    ax[2].pie(df['Block Size'], labels=df['Date'], autopct='%1.1f%%')
    ax[2].set_title('Block Size')

    plt.show()


halving_chart_graphs()

"""
9. Create a blockchain network with 4 added blocks. You must use the user input to input your data.
"""
import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0, datetime.datetime.now(), "Genesis Block", "0"))

    def get_previous_block(self):
        return self.chain[-1]

    def add_block(self, block):
        previous_block = self.get_previous_block()
        block.previous_hash = previous_block.hash
        block.hash = block.hash_block()
        self.chain.append(block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.hash_block():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print({"idex": block.index, "timestamp": str(block.timestamp), "data": block.data, "previous_hash": block.previous_hash, "hash": block.hash})

blockchain = Blockchain()
for i in range(4):
    data = input(f"{i+1}) Enter your data: ")
    blockchain.add_block(Block(i, datetime.datetime.now(), data, blockchain.get_previous_block().hash))

blockchain.print_chain()

"""
10. Create your own payment system, it could be centralize or decentralize system.
"""
class PayementSystem:
    def __init__(self):
        self.transactions = []
        self.users = {}

    def add_user(self, username, password):
        self.users.update({ username: hashlib.sha256(password.encode()).hexdigest()})

    def exists(self, username):
        return username in self.users

    def print_transactions(self):
        for index, transaction in enumerate(self.transactions):
            print(f"{index + 1}: sender => {transaction.username} reciever: {transaction.payement_to} ammount: {transaction.ammount}")

    def make_payement(self, username, ammount, payement_to):
        self.transactions.append({"sender": username, "reciever": payement_to, "ammount": ammount})


payement_sys = PayementSystem()

start = True
while start:
    print("""
    Welcome to our Payement system\n
    1. create user
    2. send money
    3. exit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if payement_sys.exists(username):
            print("Username exists already")
            exit(-1)
        payement_sys.add_user(username, password)
    elif choice == 2:
        sender = input("Enter your name: ")
        reciever = input("Enter recipient: ")
        amt = input("Enter ammount: ")
        payement_sys.make_payement(sender, amt, reciever)
        print("sent!")
    elif choice == 3:
        break

    else:
        print("Invalid choice")
        exit(-1)




    