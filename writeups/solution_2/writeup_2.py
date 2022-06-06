import json
from web3 import Web3, HTTPProvider

client = Web3(HTTPProvider("http://awesome.chall.seetf.sg:40002/"))

target = "0x8E13df48763E76168e70ad3c49F54b3ab3636e5D"

with open("challange2_abi.json", "r") as file:
    target_abi = json.load(file)

target_contract = client.eth.contract(address=target, abi=target_abi)

balance_amount_byte = client.eth.get_storage_at(target, 0)

balance_amount = int.from_bytes(balance_amount_byte, "big")

target_balance = 1337

print(f"The target balance amount is: {balance_amount}.")

increase_amount = target_balance - balance_amount

print(f"The target increasing amount is: {increase_amount}.")
