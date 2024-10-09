# first install pyvicon 
# python3 -m pip install pyvicon

import pyvicon
import time

# Replace 'your_vicon_server' with your actual Vicon server's IP or hostname
client = pyvicon.ViconClient('your_vicon_server')

# Ensure the client is connected to the Vicon system
if client.is_connected():
    print("Connected to Vicon system.")

# The name of the object being tracked
# Replace 'UAV' with the name of your UAV object in Vicon Tracker
object_name = 'UAV'

try:
    while True:
        # Fetch XYZ position in the Vicon world frame
        position = client.get_segment_global_translation(object_name)
        
        # Fetch Euler angles (roll, pitch, yaw) in degrees
        rotation = client.get_segment_global_rotation_euler_xyz(object_name)
        
        if position and rotation:
            # Print the XYZ position and roll, pitch, yaw
            print(f"Position: X: {position[0]:.3f}, Y: {position[1]:.3f}, Z: {position[2]:.3f}")
            print(f"Rotation: Roll: {rotation[0]:.3f}, Pitch: {rotation[1]:.3f}, Yaw: {rotation[2]:.3f}")
        
        # Sleep for a bit to avoid overwhelming the system
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Terminating connection to Vicon.")
    client.disconnect()
