#########################################################################
# File       : send_udp.py
# Authors    : Surafel Anshebo, Giri Mugundan Kumar
# contant    : surafela@vt.edu, girimugundan@vt.edu 
# Description: This code reads the data from the vicon tracker and sends
#              the data via udp to the raspberry pi 3B+ on the s500 drone
#              used by Surafel for BVLOS               
#########################################################################


# Sender script (Windows 7 desktop)
import socket
import time

# Import the vicon sdk
from vicon_dssdk import ViconDataStream

# ************************************************************
# Config
# ************************************************************
# Function to get Raspberry Pi IP dynamically
def get_pi_ip():
    # Assuming the Pi is connected to the same network and using hostname
    try:
        return socket.gethostbyname("raspberrypi.local")
    except socket.gaierror:
        print("Error: Could not resolve Raspberry Pi hostname.")
        exit(1)

# Store the program start time
start_time = time.perf_counter()

# Function to get the elapsed time since the program started
def get_program_time():
    return time.perf_counter() - start_time

# Function to get the elapsed time in milliseconds since the program started
def get_program_time_ms():
    return (time.perf_counter() - start_time) * 1000  # Convert seconds to milliseconds

hostName = "localhost:801" # IP address of the computer running Vicon Tracker

# Setup UDP socket
udp_ip = get_pi_ip()  # Get Raspberry Pi's IP address dynamically
udp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ************************************************************
# Initialize
# ************************************************************
# Hardcode the subject name from the vicon tracker app.
subjectName = 's500'

client = ViconDataStream.Client()
client.Connect(hostName)

client.EnableSegmentData()
client.SetBufferSize(1) # Always return the most recent frame
client.SetStreamMode(ViconDataStream.Client.StreamMode.EServerPush)
# Set it to NED frame as the pixhawk requires data in the NED frame for fusion
client.SetAxisMapping(
    ViconDataStream.Client.AxisMapping.EForward,
    ViconDataStream.Client.AxisMapping.ERight,
    ViconDataStream.Client.AxisMapping.EDown)  # Set the global up axis to Z-DOWN

# ************************************************************
# Main Program
# ************************************************************
# Continuously get frames
try:
    while True:
        # Retrieve a frame from Vicon Tracker
        client.GetFrame()       

        # Decode frame - object pose
        # We know that the subject name is s500 that we have set in 
        # the tracker system. Therfore we can hardcode that data in
        
        # Get the segment names
        segmentNames = client.GetSegmentNames(subjectName)
        segmentName = segmentNames[0]

        # Get the position and quaternion data
        ret_P = client.GetSegmentGlobalTranslation(subjectName, segmentName)
        ret_Q = client.GetSegmentGlobalRotationQuaternion(subjectName,segmentName)

        # Extract the position and quaternion data
        P = ret_P[0]
        Q = ret_Q[0]
        isOccluded = ret_P[1] or ret_Q[1]

        # Get the system timestamp of the data
        timestamp = get_program_time()

        # Package the data to a string that we can send to the raspberry pi 
        # in the format R, time, x, y, z, q0, q1, q2, q3
        # We need the R in the start to verify that the data is true. Here
        # I have put in R for ROS since the raspberry pi runs on ROS - Giri
        
        # Using f-string to format the string as "R,t,x,y,z,q0,q1,q2,q3"
        message = f"R,{timestamp},{P[0]},{P[1]},{P[2]},{Q[0]},{Q[1]},{Q[2]},{Q[3]}"

        # Send message
        sock.sendto(message.encode(), (udp_ip, udp_port))
        print(f"Sent: {message}")   

        # Uncomment to debug - Giri
        # print(subjectName)
        # print('Frame Rate:   ', client.GetFrameRate())
        # print('Is Occluded:     ', isOccluded)
        # print('Translation:     ', P)
        # print('Quaternion Matrix: ', Q)
    print()

except KeyboardInterrupt:
    print("Program interrupted by user. Exiting...")


# ************************************************************
# End
# ************************************************************
client.Disconnect()
