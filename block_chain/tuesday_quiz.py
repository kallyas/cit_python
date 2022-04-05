import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import cv2
import requests
import json
import hashlib
from datetime import datetime
from urllib3.util import parse_url


"""
1. create a blobkchain that sends payements and recieve payements from the user
"""

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.new_block(previous_hash=1, proof=100)
        self.balance = 0

    def register_node(self, address):
        parsed_url = parse_url(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            if block['previous_hash'] != self.hash(last_block):
                return False

            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def get_balance(self, address):
        for block in self.chain:
            for transaction in block['data']:
                if transaction['sender'] == address:
                    self.balance -= transaction['amount']
                if transaction['recipient'] == address:
                    self.balance += transaction['amount']

        return self.balance

    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None

        max_length = len(self.chain)

        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'data': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    def recieve_payment(self, sender, recipient, amount):
        self.new_transaction(sender, recipient, amount)
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"



"""
2. create your own store chart with rows and columns inside a dataframe
The columns are each items you are selling in your store and the
rows are the amounts of each item in each column.
"""

class Store_Chart:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        
    def data_frame(self):
        df = pd.DataFrame({
            'Products': self.rows,
            'Sales': self.columns
        })
        return df
    
    def plot_chart(self):
        df = pd.DataFrame(self.columns, index=self.rows)
        plt.title("A chart for sales of my store")
        plt.plot(df, marker='o')
        plt.show()

"""
3. That store chart you created, we want to see different graphs using
subplot function.
"""

class Plot_Graph:
    def plot_graph(self, data=None, labels=None):
        # create a subplot that fits 3 graphs in one figure
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))
        axs[0].bar(data.index, data['Sales'])
        axs[0].set_title('Bar Graph')
        axs[1].plot(data.index, data['Sales'])
        axs[1].set_title('Line Graph')
        axs[2].pie(data['Sales'], labels=labels, autopct='%1.1f%%')
        axs[2].set_title('Pie Graph')


"""
3. download an image with opencv and make that image smaller 
"""

def download_image(url):
    response = requests.get(url)
    img = cv2.imdecode(np.fromstring(response.content, np.uint8), cv2.IMREAD_COLOR)
    return img


def resize_image(img, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = img.shape[:2]

    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(img, dim, interpolation=inter)
    return resized


def show_image(original, resized):
    cv2.imshow("Original", original)
    cv2.imshow("Resized", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""
5. create a user login. user could create a password and 
the output will display login successful
"""

def get_user():
    return {
        'username': 'admin',
        'password': 'admin'
    }