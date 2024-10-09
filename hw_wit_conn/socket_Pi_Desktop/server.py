#Run this on Pi - server

import socket

# Create a socket object (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to all available network interfaces, on port 12345
server_socket.bind(('0.0.0.0', 12345))

# Start listening for incoming connections (allow 1 connection at a time)
server_socket.listen(1)
print("Server is listening on port 12345...")

# Accept an incoming connection
connection, client_address = server_socket.accept()
print(f"Connected to client at: {client_address}")

# Receive data from the client (max buffer size 1024 bytes)
data = connection.recv(1024).decode()
print(f"Received from client: {data}")

# Send a response to the client
connection.send("Hello, Client!".encode())

# Close the connection
connection.close()
