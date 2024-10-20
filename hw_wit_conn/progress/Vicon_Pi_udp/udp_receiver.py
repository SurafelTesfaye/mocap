#########################################################################
# File       : udp_receiver.py
# Authors    : Surafel Anshebo, Giri Mugundan Kumar
# contant    : surafela@vt.edu, girimugundan@vt.edu 
# Description: This code receives the udp datagram from the vicon pc and 
#               send the data to the pixhawk and also logs it
#########################################################################

import socket
import os
from datetime import datetime

# ************************************************************
# Config
# ************************************************************
# Setup UDP socket
udp_ip = "0.0.0.0"  # Listen on all interfaces
udp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

print(f"Listening on port {udp_port}...")

# Generate the log file path with the desired structure
current_time = datetime.now()

# Define directory structure in the home folder:
#       /logs/yyyy_mm_dd/flight_run_hh_mm_ss/
log_dir = current_time.strftime("/home/pi/logs/%Y_%m_%d/flight_run_%H_%M_%S/")

# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Define log file name
log_file = os.path.join(log_dir, "mocap_lop.log")

# Check if the file already exists to avoid rewriting headers
if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        # Write the header line
        f.write("t,x,y,z,q0,q1,q2,q3\n")

# ************************************************************
# Main Program
# ************************************************************
# Continuously get frames
while True:
    # Receive message
    data, addr = sock.recvfrom(1024)

    # Uncomment this to see if the data is right - Giri
    # print(f"Received message from {addr}: {data.decode()}")

    # Get the string data
    string = data.decode()

    # Split the string by commas
    values = string.split(',')

    # Extract the values (ignoring the first element 'R')
    t = float(values[1])     # Time [s]
    x = float(values[2])     # x [m]
    y = float(values[3])     # y [m]
    z = float(values[4])     # z [m]
    q0 = float(values[5])    # q0 [-]
    q1 = float(values[6])    # q1 [-]
    q2 = float(values[7])    # q2 [-]
    q3 = float(values[8])    # q3 [-]

    # Optionally, you can print the values to check - Giri
    print(f"t: {t}")
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    print(f"q0: {q0}")
    print(f"q1: {q1}")
    print(f"q2: {q2}")
    print(f"q3: {q3}")

    # Log the values to the .log file - This is the  data for
    # the log file in the home folder 
    with open(log_file, 'a') as f:
        # Append the values to the file in CSV format
        f.write(f"{t},{x},{y},{z},{q0},{q1},{q2},{q3}\n")
