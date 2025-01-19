import hashlib
import requests
from datetime import datetime
import json
import urllib3
from typing import List, Dict, Any, Optional, Set


class Block:
    def __init__(self, index: int, timestamp: datetime, data: Any, previous_hash: str) -> None:
        """
        Initializes a new block.

        Args:
            index (int): The index of the block in the blockchain.
            timestamp (datetime): The timestamp when the block was created.
            data (Any): The data stored in the block.
            previous_hash (str): The hash of the previous block in the blockchain.
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self) -> str:
        """
        Generates the SHA-256 hash of the block.

        Returns:
            str: The SHA-256 hash of the block.
        """
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


class BlockChain:
    def __init__(self) -> None:
        """
        Initializes a new blockchain.
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
        parsed_url = urllib3.util.parse_url(address)
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
        new_chain: Optional[List[Dict[str, Any]]] = None

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

    def new_block(self, proof: int, previous_hash: Optional[str] = None) -> Dict[str, Any]:
        """
        Creates a new block and adds it to the blockchain.

        Args:
            proof (int): The proof given by the Proof of Work algorithm.
            previous_hash (Optional[str]): Hash of the previous block.

        Returns:
            Dict[str, Any]: The new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.utcnow(),
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

    def proof_of_stakes(self, last_proof: int) -> int:
        """
        Placeholder for Proof of Stake Algorithm:
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


def main() -> None:
    """
    Main function to demonstrate the blockchain.
    """
    blockchain = BlockChain()
    print(blockchain.chain)

    blockchain.new_transaction(sender="0", recipient="1", amount=1)
    blockchain.new_transaction(sender="0", recipient="2", amount=2)

    print(blockchain.new_block(proof=100, previous_hash="1"))
    print(blockchain.chain)


if __name__ == '__main__':
    main()
