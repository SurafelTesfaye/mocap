# Sender script (Windows 7 desktop)
import socket
import time

# Function to get Raspberry Pi IP dynamically
def get_pi_ip():
    # Assuming the Pi is connected to the same network and using hostname
    try:
        return socket.gethostbyname("raspberrypi.local")
    except socket.gaierror:
        print("Error: Could not resolve Raspberry Pi hostname.")
        exit(1)

# Setup UDP socket
udp_ip = get_pi_ip()  # Get Raspberry Pi's IP address dynamically
udp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Create a message with timestamp
    timestamp = time.time()
    message = f"Timestamp: {timestamp}"
    
    # Send message
    sock.sendto(message.encode(), (udp_ip, udp_port))
    print(f"Sent: {message}")
    
    # Wait before sending the next message
    time.sleep(1)  # Send a message every second
