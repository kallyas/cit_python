# create CIT coin crypto currency

import hashlib
from datetime import datetime
import json
import requests
from urllib3.util import parse_url
from flask import Flask, jsonify, request


class CITcoin:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()
        self.new_block(previous_hash=1, proof=100)

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
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

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

    def mine_block(self):
        last_block = self.last_block
        last_proof = last_block['proof']
        proof = self.proof_of_work(last_proof)

        previous_hash = self.hash(last_block)
        block = self.new_block(proof, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash']
        }

        return response

    

    
def main():
    # Create a CIT coin
    cit_coin = CITcoin()

    # Create a web app
    app = Flask(__name__)

    # Register a node
    @app.route('/register_node', methods=['POST'])
    def register_node():
        values = request.get_json()

        nodes = values.get('nodes')
        if nodes is None:
            return "Error: Please supply a valid list of nodes", 400

        for node in nodes:
            cit_coin.register_node(node)

        response = {
            'message': 'New nodes have been added',
            'total_nodes': list(cit_coin.nodes)
        }

        return jsonify(response), 201

    # Get the full chain
    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': cit_coin.chain,
            'length': len(cit_coin.chain)
        }
        return jsonify(response), 200

    # Mine a new block
    @app.route('/mine', methods=['GET'])
    def mine():
        last_block = cit_coin.last_block
        last_proof = last_block['proof']
        proof = cit_coin.proof_of_work(last_proof)
        node_identifier = request.remote_addr

        cit_coin.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1
        )

        previous_hash = cit_coin.hash(last_block)
        block = cit_coin.new_block(proof, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash']
        }

        return jsonify(response), 200

    # Add a new transaction to the list of transactions
    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        values = request.get_json()

        # Check that the required fields are in the POST'ed data
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return 'Missing values', 400

        # Create a new transaction
        index = cit_coin.new_transaction(values['sender'], values['recipient'], values['amount'])

        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201

    # Run the app
    app.run(host='localhost', port=8000)


if __name__ == '__main__':
    main()