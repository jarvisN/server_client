import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = ''       # IP host 
port = 12345                # Reserve a port for your service.
s.connect((host, port))
print(s.recv(1024).decode())
print("ok")
