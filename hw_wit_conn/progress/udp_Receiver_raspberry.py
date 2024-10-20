# Receiver script (Raspberry Pi)
import socket

# Setup UDP socket
udp_ip = "0.0.0.0"  # Listen on all interfaces
udp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

print(f"Listening on port {udp_port}...")

while True:
    # Receive message
    data, addr = sock.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode()}")
