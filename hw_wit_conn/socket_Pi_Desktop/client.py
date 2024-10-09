import socket

# Server (Raspberry Pi) IP address and port
UDP_IP = "192.168.x.x"  # Replace with the IP address of your Raspberry Pi
UDP_PORT = 12345        # The port used by the server

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Message to send to the server
message = "Hello from UDP client!"

# Send the message to the server
client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))

# Optional: receive a response from the server
data, server = client_socket.recvfrom(1024)  # Buffer size is 1024 bytes
print(f"Received response from server: {data.decode()}")

# Close the socket
client_socket.close()
