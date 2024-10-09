# Desktop - server

import socket

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Bind to any IP and port 12345
server_socket.listen(1)

print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024)  # Receive data from client
    if not data:
        break
    print(f"Received: {data.decode()}")
    conn.sendall(b"Message received")  # Acknowledge the message

conn.close()
server_socket.close()
