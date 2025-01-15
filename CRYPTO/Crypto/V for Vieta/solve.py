import socket, re, json
from sympy import integer_nthroot

def LHS(x: int, y: int) -> int:
    return x**2 + x*y + y**2
def RHS(x: int, y: int) -> int:
    return 2*x*y + 1
def payload(k: int) -> str:
    a, b = k * (2*k*k - 1), k
    while a.bit_length() <= 2048 or b.bit_length() <= 2048:
        assert LHS(a, b) % RHS(a, b) == 0
        a, b = (2*k*k - 1) * a - b, a
    return json.dumps({"a": a, "b": b})
def find_k(data: bytes) -> int:
    pattern = r'"k":\s*(\d+)'

    # Search for the pattern in the data
    match = re.search(pattern, data.decode())

    # Extract the value of k if a match is found
    if match:
        k = int(match.group(1))
        return k
    else:
        return None


host = "2024.ductf.dev"
port = 30018

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(4096)
while True:
    k = integer_nthroot(y=find_k(data=data), n=2)[0]
    print(k)
    s.sendall(payload(k).encode() + b"\n")
    data = s.recv(4096)
    print(data)
