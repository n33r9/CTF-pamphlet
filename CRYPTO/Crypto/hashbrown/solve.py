import re
import time
from Crypto.Cipher import AES
import socket

def aes(block: bytes, key: bytes) -> bytes:
    assert len(block) == len(key) == 16
    return AES.new(key, AES.MODE_ECB).encrypt(block)

def pad(data):
    padding_length = 16 - len(data) % 16
    return data + b"_" * padding_length

def hash_state(data: bytes, initial_state: str):
    data = pad(data)
    state = bytes.fromhex(initial_state)

    for i in range(0, len(data), 16):
        block = data[i : i + 16]
        state = aes(block, state)

    return state 

def extract_components(input_text):
    message_match = re.search(r"b'(.*?)'", input_text, re.DOTALL)
    message = message_match.group(1) if message_match else None

    hex_match = re.search(r'as hex:\n([\da-fA-F\n]+)', input_text)
    hex_value = hex_match.group(1).replace('\n', '') if hex_match else None

    signature_match = re.search(r'Signature:\n([a-fA-F\d]+)', input_text)
    signature = signature_match.group(1) if signature_match else None

    return message, hex_value, signature

def main():
    host, port = "challs.pwnoh.io", 13419

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(2048).decode()
        time.sleep(1)
        data += s.recv(2048).decode()
        print(data)

        message, hex_value, signature = extract_components(data)
        print(f"{message = }")
        print(f"{hex_value = }")
        print(f"{signature = }")

        data = b"french fry"
        craft_mess = pad(bytes.fromhex(hex_value)) + data
        craft_mess = craft_mess.hex().encode() + b"\n"
        print(craft_mess)
        s.sendall(craft_mess)
        print(s.recv(1024))

        new_sign = hash_state(data, signature)
        s.sendall(new_sign.hex().encode() + b"\n")
        print(s.recv(1024))
        print(s.recv(1024))
        print(s.recv(1024))

if __name__ == "__main__":
    main()