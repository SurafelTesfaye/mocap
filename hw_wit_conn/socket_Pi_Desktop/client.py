import socket

# Create a socket object (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server IP address (replace with the IP address of your server)
server_ip = '192.168.1.10'  # Replace with your Raspberry Pi IP address
server_port = 12345

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to server.")

# Send a message to the server
client_socket.send("Hello, Server!".encode())

# Receive response from the server
response = client_socket.recv(1024).decode()
print(f"Received from server: {response}")

# Close the connection
client_socket.close()
