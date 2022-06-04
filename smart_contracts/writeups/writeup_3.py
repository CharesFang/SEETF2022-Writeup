from sha3 import keccak_256
from web3 import Web3, HTTPProvider

client = Web3(HTTPProvider("http://awesome.chall.seetf.sg:40002/"))

target = "0xeb22BF8C59eA3f98081F9a8D188f2737Ec5c153A"
# target = '0xda925A0e6AcE9fb2020fcC695aF192786dd0330A'

address_bytes = client.eth.get_storage_at(target, 0)
owner_address = hex(int.from_bytes(address_bytes, 'big'))
print(f"Owner address: {owner_address}.")


map_basis_slot = client.eth.get_storage_at(target, 1)
map_basis = hex(int.from_bytes(map_basis_slot, 'big'))
print(f"Map basis address: {map_basis}.")

time_stamp_slot = client.eth.get_storage_at(target, 2)
time_stamp = hex(int.from_bytes(time_stamp_slot, 'big'))
print(f"Time stamp address: {time_stamp}.")

# time_stamp_slot = client.eth.get_storage_at(target, keccak_256(client.toBytes(1)+client.toBytes(0)))
# time_stamp = hex(int.from_bytes(time_stamp_slot, 'big'))
# print(f"Owner address: {time_stamp}.")

map_1_address = client.keccak(bytes.fromhex("0"*63 + "1" + "0"*63 + "0")).hex()
# map_1_address = keccak_256(bytes.fromhex("0"*63 + "0" + "0"*63 + "1")).hexdigest()
print(map_1_address)
map_1_slot = client.eth.get_storage_at(target, map_1_address)
map_basis = hex(int.from_bytes(map_basis_slot, 'big'))
print(f"Map basis address: {map_basis}.")

# t = keccak_256(bytes.fromhex('00000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000000000000002')).hexdigest()
# bytesss = client.eth.get_storage_at(target, t)
# map_basis = hex(int.from_bytes(bytesss, 'big'))
# print(f"Map basis address: {map_basis}.")