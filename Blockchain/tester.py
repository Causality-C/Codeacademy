''' 
    Tester creates a blockchain ledger for the use of keeping track of soybeans transactions between a group of four friends: Jim, Warren, Samantha, and Emily
    Read in data.txt which contains N transactions. 
    Each of the N lines contains 3 parameters:
    - The name of the sender
    - The name of the receiver
    - The amount of soybeans in bushels
    data.txt:
    4
    Jim Warren 50
    Warren Samantha 140
    Emily Jim 100
    Samantha Emily 90

    Tester also demonstrates that any tampering of the blockchain would be transparent for all to see.
'''
from blockchain import Blockchain
import datetime
file = open("data.txt", "r")
cases = file.readline()

transactions = []

#Retrieve transaction data
for i in range(0, int(cases)):
    data = file.readline().split(" ")
    temp = {"sender": data[0], "reciever": data[1], "bushels": data[2].rstrip()}
    transactions.append(temp)

soyChain = Blockchain()
print("Initialization of Blockchain:")
soyChain.print_blocks()
proof = []
#Adding transaction 1 block per transaction
first_time = datetime.datetime.now()
for i in range(0, int(cases)):
    proof.append(soyChain.add_block(transactions[i])[0])
later_time = datetime.datetime.now()
difference = later_time-first_time 


#How long did it take to add N blocks with a difficulty of 5?
print("Adding Blocks:")
soyChain.print_blocks()
print("The addition of {} blocks took {} seconds.\n".format(int(cases),difference.total_seconds()))
print("Proof of Work:")
for i in proof:
    print(i)
print("\n")
soyChain.validate_chain()


#Emily tries to hack the ledger
soyChain.chain[2].transactions = {"sender": 'Samantha', "reciever": 'Emily', "bushels": '45'}
soyChain.chain[3].transactions = {"sender": 'Jim', "reciever": 'Emily', "bushels": '18'}
soyChain.print_blocks()
soyChain.validate_chain()
