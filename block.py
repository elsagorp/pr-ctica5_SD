from datetime import date
import hashlib
from hmac import digest   							# For hash checksum digest function SHA256

import time



class Block:
    

    
    def __init__(self,index, transactions, previous_hash):
        self.index = index
        self.timestamp      = time.ctime()
        self.transactions 	 = transactions
        self.transactions_count  = len(transactions)
        self.previous_hash 		 	 = previous_hash
        self.nonce, self.hash  	 = self.compute_hash_with_proof_of_work()
        
        

    def __str__(self):
        return ("Block: \n Index:" + str(self.index) + "\n Hash: " + str(self.hash) +"\n Timestamp: " + str(self.timestamp) + "\n Transactions: " + str(self.transactions) + "\n Transactions count: " + str(self.transactions_count) + "\n Nonce: " + str(self.nonce) +  "\n Previous_hash: " + str(self.previous_hash) +"\n--------------")




    def compute_hash_with_proof_of_work(self):
            difficulty="00"
            nonce = 0
            while True:
                hash = self.calc_hash_with_nonce(nonce)
                if hash.startswith(difficulty):
                    return [nonce, hash]
                
                nonce +=1
        
        
    def calc_hash_with_nonce(self,nonce):
    
        sha = hashlib.sha256()
        sha.update((str(nonce)+str(self.index) + str(self.timestamp) + str(self.transactions)+ str(self.transactions_count) + str(self.previous_hash)).encode('utf-8'))

        return sha.hexdigest()

    def first(  transactions ):    
        return Block ( 0,transactions, "0")


    def next( previous, transactions ):
        return Block( previous.index+1, transactions, previous.hash )
