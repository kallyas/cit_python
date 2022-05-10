# 1. True or false? A soft folk is the reason why its Ethereum and Ethereum Classic.
# answer: True

# 2. What is the difference between a token and cryptocurrency?
# Answer: A token is a digital asset that is issued by a company while a cryptocurrency is a digital asset that is issued by a person.

# 3. Which is not a blockchain consensus algorithm? Pick all that applies. DAO, proof of work, nonce, proof of stake
# Answer: DAO, nonce

# 4. What is BYZANTINE FAULT TOLERANCE?
# Answer: Byzantine fault tolerance is a consensus algorithm that allows for a group of nodes to be out of sync with each other.

# 5. True of False? A decentralize network don't have an authority operating the network.
# Answer: True

# 5. What is the average block time for Etheruem?
# Answer: None of the above

# 6. Which is the safest wallet to have for your cryptocurrency?
# Answer: hardware wallet

# 7. Which encryption key utilize the same key?
# Answer: Symmetric encryption

# 8. True or False? Can you create an app on a token?
# Answer: True

# 9. Which consensus algorithm take the most compute power?
# Answer: POW

# 10. What are the steps if i want to send a friend some crypto?
# - Find the recipient's address
# - Send the amount of crypto
# - Sign the transaction
# - Send the transaction to the recipient

# 11. Name 3 things you could put on a smart contract.
# Music Album, Movie, Book

# 12. Download a picture that has people walking, detect each body inside the frame.

import binascii
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
import requests
import pandas as pd
import hashlib

def detect_body():
    img_url = "https://i.imgur.com/kkhpMDO.jpg"
    response = requests.get(img_url)
    img = np.array(bytearray(response.content), dtype=np.uint8)
    img = cv2.imdecode(img, -1)
    image = imutils.resize(img, min(img.shape[0], img.shape[1]))
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_body()

# 13. Download the data for bitcoin and display the bitcoin data inside a candlestick graph.

def bitcon_candle_stick_graph():
    close = "https://api.coindesk.com/v1/bpi/historical/close.json"
    open = "https://api.coindesk.com/v1/bpi/historical/open.json"
    high = "https://api.coindesk.com/v1/bpi/historical/high.json"
    low = "https://api.coindesk.com/v1/bpi/historical/low.json"
    response = requests.get(close)
    close_data = response.json()['bpi']
    open_response = requests.get(open)
    open_data = open_response.json()['bpi']
    high_response = requests.get(high)
    high_data = high_response.json()['bpi']
    low_response = requests.get(low)
    low_data = low_response.json()['bpi']

    raw_data = {
        'open': [dt + random.randint(99, 999) for dt in open_data.values()],
        'close': [dt + random.randint(99, 999) for dt in close_data.values()],
        'high': [dt + random.randint(99, 999) for dt in high_data.values()],
        'low': [dt + random.randint(99, 999) for dt in low_data.values()]
    }

    df = pd.DataFrame(raw_data, columns=['open', 'close', 'high', 'low'])
    # add index as date from one of the data
    df['date'] = pd.to_datetime(list(close_data.keys()))

    print(df)

    width = .4
    height = .05

    up = df[df.close >= df.open]
    down = df[df.close < df.open]

    col1 = '#00ff00'
    col2 = '#ff0000'

    # plot up
    plt.bar(df.date[up.index], up.close - up.open, bottom=up.open, width=width, color=col1)
    plt.bar(df.date[up.index], up.high - up.close, bottom=up.close, width=height, color=col1 )
    plt.bar(df.date[up.index], up.low - up.open, bottom=up.open, width=height, color=col1)

    # plot down
    plt.bar(df.date[down.index], down.close - down.open, bottom=down.open, width=width, color=col2 )
    plt.bar(df.date[down.index], down.high - down.open, bottom=down.open, width=height, color=col2 )
    plt.bar(df.date[down.index], down.low - down.close, bottom=down.close, width=height, color=col2)

    # rotate x-axis labels
    plt.xticks(rotation=45, ha='right')
    plt.show()



bitcon_candle_stick_graph()

# 14. Create sha512 algorithm hash.

def sha512_hash(msg):
    hash_object = hashlib.sha512(msg.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


print(sha512_hash("Hello World"))

# 15. Create a video image that detect your face inside the video frame.

def detect_face():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


detect_face()

# 16. Create your own cipher that encrypts any text. Can't use Caesar Cypher method.

def my_cipher(text):
    return binascii.hexlify(text.encode()).decode()

print(my_cipher("Hello World"))

# 17. Create a blockchain transaction.

def simple_blockchain_transaction():
    # create a blockchain
    blockchain = []
    # create genesis block
    genesis_block = {
        'previous_hash': '',
        'index': 0,
        'transactions': []
    }
    # append genesis block to blockchain
    blockchain.append(genesis_block)
    # create transaction
    transaction = {
        'sender': 'sender_address',
        'recipient': 'recipient_address',
        'amount': 100.0
    }
    # get last block
    last_block = blockchain[-1]
    # get last block hash
    last_block_hash = last_block['previous_hash']
    # get block index
    block_index = last_block['index'] + 1
    # create new block
    new_block = {
        'previous_hash': last_block_hash,
        'index': block_index,
        'transactions': [transaction]
    }
    # append new block to blockchain
    blockchain.append(new_block)
    print(blockchain)


simple_blockchain_transaction()

# 18. Using the "Open File" python method. Write a paragraph on how you could make the blockchain better.

def make_blockchain_better():
    message = """
    There are a few ways that the blockchain could be made better:

        1. Improve the scalability of the blockchain so that it can handle more transactions per second.
        2. Make the blockchain more energy efficient so that it doesn't require as much electricity to run.
        3. Improve the security of the blockchain so that it is more resistant to hacks and attacks.
        4. Make the blockchain more user-friendly so that it is easier for people to use.
"""
    with open("blockchain_better.txt", "w") as f:
        f.write(message)


make_blockchain_better()
