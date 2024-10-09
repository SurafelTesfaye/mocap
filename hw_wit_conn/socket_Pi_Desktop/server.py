import socket

# Server (Raspberry Pi) settings
UDP_IP = "0.0.0.0"  # Listen on all available network interfaces
UDP_PORT = 12345    # Port to listen on

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_socket.bind((UDP_IP, UDP_PORT))
print(f"UDP server listening on port {UDP_PORT}...")

# Listen for incoming messages
while True:
    data, client_address = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message from {client_address}: {data.decode()}")

    # Optional: send a response to the client
    response = "Hello from UDP server!"
    server_socket.sendto(response.encode(), client_address)
