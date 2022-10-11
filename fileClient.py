from socket import socket, AF_INET, SOCK_STREAM
import sys
import hashlib

server_addr = ('localhost', 10000)

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "input.txt"

with socket(AF_INET,SOCK_STREAM) as client:
    with open(file, "rb") as f: #binĂĄris mĂłdban nyitjuk meg
        client.connect(server_addr)
        l = f.read(10)
        while l:
            client.sendall(l)
            l = f.read(10)
        print("Elküldtem a fájlt")

with socket(AF_INET,SOCK_STREAM) as client:
    with open(file, 'r') as f:
        client.connect(server_addr)
        content = f.read()
        hashed = hashlib.md5(content.encode())
        print(hashed.hexdigest())
        client.send(bytearray(hashed.hexdigest().encode()))
        print('Elküldtem a hashet')
