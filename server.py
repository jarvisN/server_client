import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.1.34'       # IP host 
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
print("Start")
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   data = 'test_12345'
   c.send(data.encode())
   c.close()                # Close the connection