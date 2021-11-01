import hashlib
from time import gmtime
import time


class Block:  		
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = None

    def calc_hash(self):
        sha = hashlib.sha256()
        #hash is a combination of data, timestamp and previous block's hash:
        hash_str = (str(self.data) + str(self.timestamp) + str(self.previous_hash)).encode('utf-8')  
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash


class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,string):   # append a block with string as data
        timestamp = time.gmtime()   # GMT timestamp
        
        if self.head is None:		 # if blockchain is empty, create head
            self.head = Block(timestamp,string, None) 
        
        else:				# create a new head with new hash and previous_hash from old head
            previous_hash = self.head.get_hash()  
            block = Block(timestamp,string, previous_hash)
            block.previous = self.head
            self.head = block
        self.size += 1

    def printchain(self):		# print each block's data, hash and previous hash
        node = self.head
        index = self.size
        while node:
            print("block: {}, data: {} \n , hash: {} \n , previous hash: {} \n , time: {} \n".format(index,node.data,node.hash, node.previous_hash, node.timestamp))
            node = node.previous
            index -= 1
        

print("Test case 1:")

blockchain = BlockChain()
blockchain.append("Peter")
blockchain.append("Alexander")
blockchain.append("Klaus")
blockchain.append("banthafodder")
blockchain.append(2)   			
blockchain.printchain()
# Creates a blockchain and print each block's data, hash and previous hash. Edge case empty string is accepted.


print("Test case 2:")

blockchain2 = BlockChain()
blockchain2.append("Susi"), blockchain2.append("Strolch")	# edge case: two blocks created at same time have same timestamp
blockchain2.printchain()


print("Test case 3:")
blockchain3 = BlockChain()		# edge case: prints empty as there is no block in blockchain
blockchain3.printchain()
