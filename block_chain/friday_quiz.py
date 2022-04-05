# 1. What are the 3 most important components for a blockchain.
# - blockchain
# - peer-to-peer network
# - consensus algorithm

# 2. What are miners trying to solve to get the "golden nonce?"
# They are hoping to produce a hash value that meets the target and so win the block reward.

# 3. True or false? The genesis block has the previous hash and another hash
# - True

# 4.  Download a picture with cv2 then print out the array pixel.

import json
import requests
import cv2
import numpy as np
import string
import hashlib
import datetime
import pandas as pd
import random

def download_image(url):
    response = requests.get(url)
    image = np.asarray(bytearray(response.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def print_array_pixel(image):
    print(image)

url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
image = download_image(url)
print_array_pixel(image)

# 5. Download a picture with cv2 and turn the picture to a grey scale frame.

def download_image_to_grey_scale(url):
    response = requests.get(url)
    image = np.asarray(bytearray(response.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    return image

def show_image(image):
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# github logo
github_url = 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'
github_image = download_image_to_grey_scale(github_url)
show_image(github_image)

# 6. How many characters long is a hexadecimal?
# - 8

# 7. Create a Caesar Cypher using the user input.

def ceaser_cipher(text, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

user_text = input('Enter text: ')
user_shift = int(input('Enter shift: '))
output = ceaser_cipher(user_text, user_shift)
print(f"Your ceaser cipher is: {output}")

# 8. What would cause an avalanche effect to the blockchain network?
# - The network is not connected to the internet.

# 9. In OpenCv what is the three numbers in the array represent?
# blue,green,red

# 10. Create a blockchain that prints out the nonce,hash,and data.
class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.nonce = 0
        self.date = str(datetime.datetime.now())

    def calculate_hash(self):
        sha = hashlib.sha256()
        update_str = json.dumps(self.__dict__, sort_keys=True).encode()
        sha.update(update_str)
        return sha.hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __repr__(self):
        return f'Block: {self.data}'


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block('Genesis Block', '0')

    def get_previous_block(self):
        return self.chain[-1]

    def print_block_data(self):
        for block in self.chain:
            print(f'Data: {block.data}')
            print(f'Nonce: {block.nonce}')
            print(f'Date: {block.date}')
            print(f'Hash: {block.hash}')
            print(f'Previous Hash: {block.previous_hash}')
            print('-' * 20)

    def add_block(self, block, proof):
        previous_hash = self.get_previous_block().hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        return block_hash.startswith('0' * self.difficulty)

    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.calculate_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.calculate_hash()
        return computed_hash

    def get_chain(self):
        return self.chain

    def is_valid_chain(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block.previous_hash != previous_block.hash:
                return False
            previous_block = block
            block_index += 1
        return True

    def replace_chain(self, chain):
        if self.is_valid_chain(chain) and len(chain) > len(self.chain):
            self.chain = chain

block_chain = Blockchain()
block = Block('Test Block', block_chain.get_previous_block().hash)
print(block)
proof = block_chain.proof_of_work(block)
block_chain.add_block(block, proof)
print(block_chain.get_chain())
block_chain.print_block_data()

# 11. You are given a task to find all of the whole numbers below 100 that are multiples of both 3 and 5.
# Create an array of numbers below 100 that are multiples of both 3 and 5, and output it.

def find_multiples_of_both_3_and_5():
    numbers = []
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append(i)
    return numbers

multiples = find_multiples_of_both_3_and_5()
print(multiples)

# 12. Create a data frame call test_scores with 3 columns. The columns are Math, Reading ,and Science. 
# Find the mean for all three columns.

def create_data_frame():
    test_scores = pd.DataFrame(
        {
            'Math': [18, 90, 70, 60, 50, 40, 13, 20, 10],
            'Reading': [80, 90, 70, 65, 50, 40, 30, 20, 12],
            'Science': [78, 100, 70, 16, 50, 40, 30, 22, 10]
        }
    )
    return test_scores


def mean_of_all_columns(data_frame):
    return data_frame.mean()

df = create_data_frame()
print(df)
print(mean_of_all_columns(df))




