import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 3456

s.bind((host, port))

print("server listening...")

s.listen()

conn, addr = s.accept()

print (f"Connected by : {addr}")

data = conn.recv(1024)

print(f"Data received  : {data}")

s.close()