import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.proof}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", 0)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if self.is_valid_block(block, self.get_latest_block()):
            self.chain.append(block)

    def proof_of_work(self, previous_hash):
        proof = 0
        while not self.is_valid_proof(proof, previous_hash):
            proof += 1
        return proof

    def is_valid_proof(self, proof, previous_hash):
        guess = f"{proof}{previous_hash}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Difficulty: first 4 chars must be "0000"

    def is_valid_block(self, new_block, previous_block):
        if new_block.previous_hash != previous_block.hash:
            return False
        if not self.is_valid_proof(new_block.proof, new_block.previous_hash):
            return False
        return True

