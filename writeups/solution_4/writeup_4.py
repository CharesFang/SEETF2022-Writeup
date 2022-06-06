from web3 import Web3, HTTPProvider

client = Web3(HTTPProvider("http://awesome.chall.seetf.sg:40002/"))

target = "TARGET ADDRESS"

balance = client.eth.get_balance(target)

print(client.fromWei(balance, 'ether'))

