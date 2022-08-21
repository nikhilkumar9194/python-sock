from http import client
import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 3456

clientSock.connect((host, port))

clientSock.sendall(b'Hello friend!!')

data = clientSock.recv(1024)

print(f"data received : {data}")

clientSock.close()