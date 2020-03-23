#imports the Block class from block.py
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()
  
  # Generates the Genesis block
  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  # Prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {}".format(i))
      current_block.print_contents()    
  
  # Add block to blockchain `chain` taking into consideration the nonce 
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    self.chain.append(new_block)
    proof = self.proof_of_work(new_block)
    return proof, new_block
    
  # Checks if any of the blocks in the blockchain have been tampered
  def validate_chain(self):
    hacked = set()
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      
      #Updates values of hashes that have been tampered with
      if(current.hash != current.generate_hash()):
        hacked.add(i)
      if(current.previous_hash != previous.generate_hash()):
        hacked.add(i-1)
        
    if len(hacked)>0:
        hackedMessage = ""
        for j in hacked:
            hackedMessage+= str(j) + ", "
        print("Blocks {} has been tampered with.\n".format(hackedMessage[:-2]))
        return False
    else:
        print("All hashes of the blocks are valid and thus the blockchain has not been tampered with.\n")
        return True
  
  #Nonce and Proof of Work with difficulty value 5
  def proof_of_work(self,block, difficulty=5):
    proof = block.generate_hash()
    while proof[:difficulty] != '0'*difficulty:
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof