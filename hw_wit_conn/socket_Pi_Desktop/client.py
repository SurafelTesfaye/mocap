#client - laptop - or pi

import socket

# Replace 'your_desktop_ip' with the IP address of your desktop
server_ip = 'your_desktop_ip'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

message = "Hello from laptop!"
client_socket.sendall(message.encode())

data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

client_socket.close()
