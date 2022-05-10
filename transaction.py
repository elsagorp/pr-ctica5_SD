import hashlib   							# For hash checksum digest function SHA256
import pprint
import time

from block import Block

def get_transactions_data( ):
	x = 0
	new_transaction = ""
	transactions_block = []

	while new_transaction != "n":
		print( "\n") 
		print( "Enter your name for the new transaction")
		fro = input()
		print( "\n") 
		print( "What do you want to send ?")
		what = input()
		print( "\n") 
		print("How much quantity ?")
		qty  = input()
		print( "\n") 
		print("Who do you want to send it to ?")
		to 	 = input()

		transaction = {"from": fro, "to": to, 
											 "what": what, "qty": qty}
		transactions_block.append(transaction)

		print( "\n") 
		print ("Do you want to make another transaction for this block ? (Y/n)")
		new_transaction = input()

		if new_transaction == "n":
			return transactions_block
			break
		
			

