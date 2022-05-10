
import time

from block import Block
from transaction import get_transactions_data


class Blockchain:
	blockchainaux = []

	def create_first_block(self):
		i = 0
		self.blockchainaux.append(Block.first([{ "from": "Dutchgrown", "to": "Vincent", "what": "Tulip  Sunset", "qty": 10 },{ "from": "Keukenhof", "to": "Anne", "what": "Tulip Semper Augustus", "qty": 7 }]))
		print ( blockchain.blockchainaux[0])
		print( "============================")
		self.add_block()	
		
	def add_block(self):
		j = 1
		while True:
			self.blockchainaux.append(Block.next(blockchain.blockchainaux[j-1], get_transactions_data()))
			print( "============================")
			print( blockchain.blockchainaux[j])
			print( "============================")
			j += 1
   

	def launcher(self):
		print("===========================")
		print( "\n") 
		print ("Welcome to Simple Blockchain In Python")
		print( "\n") 
		time.sleep (1.5)
		print( "This program was created by Anthony Amr for and educationnal purpose")
		print( "\n") 
		time.sleep (1.5)
		print( "Wait for the genesis (the first block of the blockchain)")
		print( "\n") 
		for i in range(0,10):
			print (".")
			time.sleep (0.5) 
	
		print("===========================")
		self.create_first_block()

while True:

		
		blockchain = Blockchain()
		blockchain.launcher()


