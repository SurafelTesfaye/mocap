# trying to send this data through telemetry to the pixhawk - didnt work because dont have param file properly set or not sure

from pymavlink import mavutil
import time
import math

# Connect to Pixhawk via telemetry on COM14 (adjust the baud rate if necessary)
pixhawk = mavutil.mavlink_connection('COM14', baud=57600)
pixhawk.wait_heartbeat()
print("Connected to Pixhawk")

# Convert Vicon rotation matrix to roll, pitch, and yaw
def rotation_matrix_to_euler_angles(R):
    roll = math.atan2(R[2][1], R[2][2])
    pitch = math.atan2(-R[2][0], math.sqrt(R[2][1]**2 + R[2][2]**2))
    yaw = math.atan2(R[1][0], R[0][0])
    return roll, pitch, yaw

# Send vision position estimate to Pixhawk
def send_vision_position_estimate(translation, rotation_matrix):
    x, y, z = translation  # Vicon Translation data
    roll, pitch, yaw = rotation_matrix_to_euler_angles(rotation_matrix)  # Convert to Euler angles

    time_usec = int(time.time() * 1e6)  # Timestamp in microseconds

    pixhawk.mav.vision_position_estimate_send(
        time_usec,  # Timestamp (microseconds)
        x,          # X position (m)ch
        y,          # Y position (m)
        z,          # Z position (m)
        roll,       # Roll (rad)
        pitch,      # Pitch (rad)
        yaw         # Yaw (rad)
    )
    print(f"Sent Vision Position: X: {x}, Y: {y}, Z: {z}, Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}")

# Main loop to send data continuously
while True:
    # Example data from Vicon (replace with actual data)
    translation = (-59.148, 1986.856, 218.629)  # X, Y, Z from Vicon output
    rotation_matrix = ((0.998166, -0.060323, -0.005037),  # Rotation matrix
                       (0.060275, 0.998139, -0.009198),
                       (0.005583, 0.008877, 0.999945))

    # Send the translation and rotation data to Pixhawk
    send_vision_position_estimate(translation, rotation_matrix)

    # Sleep for a short while before sending the next frame (adjust rate as needed)
    time.sleep(0.1)  # Adjust this frequency based on your needs (10Hz is typical)
