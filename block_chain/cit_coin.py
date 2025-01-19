import hashlib
from datetime import datetime
import json
import requests
from urllib3.util import parse_url
from flask import Flask, jsonify, request
from typing import List, Dict, Any, Set

class CITcoin:
    def __init__(self) -> None:
        """
        Initializes a new instance of the CITcoin class.
        """
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Dict[str, Any]] = []
        self.nodes: Set[str] = set()
        self.new_block(previous_hash="1", proof=100)

    def register_node(self, address: str) -> None:
        """
        Adds a new node to the list of nodes.

        Args:
            address (str): Address of the node. e.g., 'http://192.168.0.5:5000'
        """
        parsed_url = parse_url(address)
        self.nodes.add(parsed_url.netloc)

    def valid_chain(self, chain: List[Dict[str, Any]]) -> bool:
        """
        Determines if a given blockchain is valid.

        Args:
            chain (List[Dict[str, Any]]): A blockchain.

        Returns:
            bool: True if valid, False otherwise.
        """
        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash'] != self.hash(last_block):
                return False

            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self) -> bool:
        """
        Consensus algorithm: resolves conflicts by replacing our chain with the longest one in the network.

        Returns:
            bool: True if our chain was replaced, False if not.
        """
        neighbours = self.nodes
        new_chain: List[Dict[str, Any]] = None

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

    def new_block(self, proof: int, previous_hash: str = None) -> Dict[str, Any]:
        """
        Creates a new block and adds it to the blockchain.

        Args:
            proof (int): The proof given by the Proof of Work algorithm.
            previous_hash (str, optional): Hash of the previous block. Defaults to None.

        Returns:
            Dict[str, Any]: The new block.
        """
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

    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """
        Creates a new transaction to go into the next mined block.

        Args:
            sender (str): Address of the sender.
            recipient (str): Address of the recipient.
            amount (float): Amount of the transaction.

        Returns:
            int: The index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self) -> Dict[str, Any]:
        """
        Returns the last block in the blockchain.

        Returns:
            Dict[str, Any]: The last block.
        """
        return self.chain[-1]

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """
        Creates a SHA-256 hash of a block.

        Args:
            block (Dict[str, Any]): Block.

        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof

        Args:
            last_proof (int): The previous proof.

        Returns:
            int: The new proof.
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the Proof:
         - Does hash(last_proof, proof) contain 4 leading zeroes?

        Args:
            last_proof (int): Previous proof.
            proof (int): Current proof.

        Returns:
            bool: True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def mine_block(self) -> Dict[str, Any]:
        """
        Mines a new block.

        Returns:
            Dict[str, Any]: The mined block.
        """
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


def main() -> None:
    """
    Main function to demonstrate the CITcoin blockchain.
    """
    cit_coin = CITcoin()
    app = Flask(__name__)

    @app.route('/register_node', methods=['POST'])
    def register_node() -> Any:
        """
        Registers a new node in the network via a POST request.

        Returns:
            Any: JSON response with status code.
        """
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

    @app.route('/chain', methods=['GET'])
    def full_chain() -> Any:
        """
        Retrieves the full blockchain.

        Returns:
            Any: JSON response with the blockchain.
        """
        response = {
            'chain': cit_coin.chain,
            'length': len(cit_coin.chain)
        }
        return jsonify(response), 200

    @app.route('/mine', methods=['GET'])
    def mine() -> Any:
        """
        Mines a new block and adds it to the blockchain.

        Returns:
            Any: JSON response with the mined block.
        """
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

    @app.route('/transactions/new', methods=['POST'])
    def new_transaction() -> Any:
        """
        Adds a new transaction to the list of transactions.

        Returns:
            Any: JSON response with the status of the transaction.
        """
        values = request.get_json()

        # Check that the required fields are in the POST'ed data
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return 'Missing values', 400

        # Create a new transaction
        index = cit_coin.new_transaction(values['sender'], values['recipient'], values['amount'])

        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201

    app.run(host='localhost', port=8000)


if __name__ == '__main__':
    main()
