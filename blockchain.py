import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Calculate the hash of the block
    def calculate_hash(self):
        string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(string.encode()).hexdigest()
    
    # Print the block
    def print_block(self):
        print("Block #{}".format(self.index))
        print("Timestamp: {}".format(self.timestamp))
        print("Data: {}".format(self.data))
        print("Previous Hash: {}".format(self.previous_hash))
        print("Hash: {}".format(self.hash))
        print()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesis_block = Block(0, time.time(), "Genesis Block", "0")
        self.chain.append(self.genesis_block)

    # Get the last block in the chain
    def get_last_block(self):
        return self.chain[-1]
    
    # Add a new block to the chain
    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    # Check if the chain is valid
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
        
        return True
    
    # Print the chain
    def print_chain(self):
        for block in self.chain:
            block.print_block()

# Create a blockchain
def main():
    blockchain = Blockchain()
    blockchain.add_block(Block(1, time.time(), "Block Sector A", "2020130002"))
    blockchain.add_block(Block(2, time.time(), "Block Sector B", "2020130001"))
    blockchain.add_block(Block(3, time.time(), "Block Sector B", "2020130017"))

    blockchain.print_chain()

    # Make blockchain invalid here
    # blockchain.chain[1].hash = ""

    if blockchain.is_chain_valid():
        print("The blockchain is valid")
    else:
        print("The blockchain is not valid")

# if __name__ == "__main__":
#     main()