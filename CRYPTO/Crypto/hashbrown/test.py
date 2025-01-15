import os
from Crypto.Cipher import AES
from Crypto.Util.number import *

secret = b'\xb3\xae\x1c\xe2\x8b\xd5c5\x92\xf6#\x87\xe3Tv3'
orig_message = 0x4772617465207468652072617720706f7461746f65732077697468206120636865657365206772617465722c20706c616365207468656d20696e746f206120626f776c20616e6420636f76657220636f6d706c6574656c7920776974682077617465722e204c65742073697420666f72203130206d696e757465732e
orig_sign = 0xf78eb5ad0831035ac699a50b26f3b322
your_message = b'rate the raw potatoes with a cheese grater, place them into a bowl and cover completely with water. Let sit for 10 minutes.____french fry'

def aes(block: bytes, key: bytes) -> bytes:
    assert len(block) == len(key) == 16
    return AES.new(key, AES.MODE_ECB).encrypt(block)

def pad(data):
    padding_length = 16 - len(data) % 16
    return data + b"_" * padding_length

def hash(data: bytes):
    data = pad(data)
    state = bytes.fromhex("f7c51cbd3ca7fe29277ff750e762eb19")
    for i in range(0, len(data), 16):
        block = data[i : i + 16]
        state = aes(block, state)
        print(state)
    return state

def sign(message, secret):
    return hash(secret + message)

def hash_state(data: bytes, initial_state: str):
    print("\n")
    data = pad(data)
    state = bytes.fromhex(initial_state)

    for i in range(0, len(data), 16):
        block = data[i : i + 16]
        state = aes(block, state)
        print(state)
    return state 

data = b'french fry'
print(long_to_bytes(orig_message))
assert orig_sign == bytes_to_long(sign(long_to_bytes(orig_message), secret))
craft_mess = pad(long_to_bytes(orig_message)) + data
assert hash_state(data, 'e6b3049ac8f0617772c254c58f8a63a7') == bytes.fromhex('452debd1c09c87babafed39e647f9123')