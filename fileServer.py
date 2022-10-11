from socket import socket, AF_INET, SOCK_STREAM
import sys
import hashlib

server_addr = ('localhost', 10000)

if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = "output.txt"

with socket(AF_INET,SOCK_STREAM) as server:
    server.bind(server_addr)
    server.listen(1)

    client, client_addr = server.accept()
    end = False
    with open(file, "wb") as f: #binĂĄris mĂłdban nyitjuk meg
        while not end:
            data = client.recv(10)
            if data:
                f.write(data)
            else:
                end = True
        print("Sikerült a fájlátvitel")

with socket(AF_INET,SOCK_STREAM) as server:
    server.bind(server_addr)
    server.listen(1)

    client, client_addr = server.accept()
    with open(file, "r") as f:
        content = f.read()
        hashed = hashlib.md5(content.encode())
        client_hash = None
        while client_hash is None:
            data = client.recv(32).decode()
            client_hash = data

        print("Sikerült az md5 kód átküldés")
        print(client_hash)
        print(hashed.hexdigest())
        if hashed.hexdigest() == client_hash:
            print("Megegyeznek")
        else:
            print("NEm egyeznek meg")
    client.close()
