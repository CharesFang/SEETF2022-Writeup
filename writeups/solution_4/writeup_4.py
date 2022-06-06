from web3 import Web3, HTTPProvider

client = Web3(HTTPProvider("http://awesome.chall.seetf.sg:40002/"))

target = "0x7991CcAa4179406623E4B5758F6a1aB37ba68984"

balance = client.eth.get_balance(target)

print(client.fromWei(balance, 'ether'))

