import hashlib
import datetime
import json
import requests
import pandas as pd
import matplotlib.pyplot as plt

"""
1. create a block chain using a dictionary
that has the data, hash, nonce and date
"""


def create_blockchain():
    blockchain = []
    return blockchain


def create_block(blockchain, data):
    block = {
        'data': data,
        'hash': None,
        'nonce': 0,
        'date': str(datetime.datetime.now())
    }
    blockchain.append(block)
    return block


def hash_block(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()


def mine_block(blockchain, difficulty=2):
    last_block = blockchain[-1]
    nonce = 0
    while True:
        nonce += 1
        block = create_block(blockchain, 'CIT')
        block['nonce'] = nonce
        block['hash'] = hash_block(block)
        if block['hash'][:difficulty] == '0' * difficulty:
            return block



"""
2. get the current bitcoin csv and plot the data
using any graph you desire
"""

def get_bitcoin_data():
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
    response = requests.get(url)
    data = response.json()['bpi']
    new_data = {
        'date': data.keys(),
        'price': data.values()
    }
    df = pd.DataFrame(new_data)
    return df


def plot_bitcoin_data(df):
    df.plot(x='date', y='price')
    plt.title('Bitcoin Price between {} and {}'.format(df.date.min(), df.date.max()))
    plt.show()


"""
3. create your own hidden cypher code that is 
totally different from the ceaser cypher
"""

def hidden_cypher(text, shift):
    return ''.join([chr((ord(c) - shift) % 26 + ord('A')) for c in text])


def decipher_hidden_cypher(text, shift):
    return ''.join([chr((ord(c) + shift) % 26 + ord('A')) for c in text])



def main():
    blockchain = create_blockchain()
    block = create_block(blockchain, 'CIT')
    print(block)
    mined_block = mine_block(blockchain, 2)
    print(mined_block)
    df = get_bitcoin_data()
    print(df)
    plot_bitcoin_data(df)
    hidden_text = hidden_cypher('CIT Uganda', 3)
    print('Hidden cyper output: {} '.format(hidden_text))
    print('Decipher Hidden text output: {}'.format(decipher_hidden_cypher(hidden_text, 3)))
    


if __name__ == '__main__':
    main()


