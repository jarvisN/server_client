import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.1.34'       # IP host 
port = 12345                # Reserve a port for your service.
s.connect((host, port))
print(s.recv(1024).decode())
print("ok")