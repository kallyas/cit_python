"""
1. Create a Blockchain wallet
"""

# create a simple blockchain wallet
import random

# only hexadecimal characters
hex_list = [str(i) for i in range(10)] + [chr(i) for i in range(97, 97 + 26)]

wallets = []
wallet = 'BTC'

for num in range(10):
    chosen = random.choice(hex_list)
    wallet += chosen
    wallets.append(wallet)


for wallet in wallets:
    print(wallet)

import random

list = ['0','1','2','3','4','5','6','7','8','9'
        'a','b','c','e','f']


wallets = []
wallet = 'BTC: '


for btcNum in range(20):
    for btcGen in range(16):
        choosen = random.choice(list)
        wallet = wallet+choosen
        if btcGen == 15:
            wallet = wallet+"*******"
            wallets.append(wallet)
            wallet = 'BTC:'
        else:
            pass

for WALLET in wallets:
    print(WALLET)

"""
2. Download the current Bitcoin csv file and print out the graph of Bitcoin's current price today

"""