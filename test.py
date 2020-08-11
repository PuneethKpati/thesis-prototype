import json
import time
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]


with open('build/contracts/Ipfs.json') as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    deployed_contract_address = contract_json['networks']['5777']['address']



# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

tx_hash = contract.functions.addHash('1','HELLLO').transact()
receipt = web3.eth.waitForTransactionReceipt(tx_hash)
message = contract.functions.getHash('1').call()
print(message)

tx_hash = contract.functions.addHash('2', 'whats up').transact()
receipt = web3.eth.waitForTransactionReceipt(tx_hash)
message = contract.functions.getHash('2').call()

print(message)	

message = contract.functions.getHash('3').call()

print(message)	
