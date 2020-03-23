import datetime
from hashlib import sha256

#changed data to transactions

class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    #Generates a hash based on the time stamp, transactions, previous hash, and nonce values.
    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()
    
    #Prints the contents of Block
    def print_contents(self):
        print("Timestamp:", self.time_stamp)
        print("Transactions:", self.transactions)
        print("Current Hash:", self.generate_hash())
        print("Previous Hash:", self.previous_hash) 
        print()