from dronekit import connect, VehicleMode
import pyvicon
import time

# Connect to the Vicon system
vicon_client = pyvicon.ViconClient('your_vicon_server')

# Connect to the drone using DroneKit
# Replace '127.0.0.1:14550' with the correct connection string (for SITL or real drone)
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# Check if Vicon and DroneKit are connected
if vicon_client.is_connected():
    print("Connected to Vicon system.")

if vehicle:
    print("Connected to drone.")

# The name of the tracked object in Vicon (e.g., UAV)
object_name = 'UAV'

def update_vicon_position(vehicle):
    """
    Continuously fetch Vicon data and update the drone's position via DroneKit.
    """
    try:
        while True:
            # Get the XYZ position and roll, pitch, yaw
            position = vicon_client.get_segment_global_translation(object_name)
            rotation = vicon_client.get_segment_global_rotation_euler_xyz(object_name)
            
            if position and rotation:
                # Print XYZ and angular data
                print(f"Position: X: {position[0]:.3f}, Y: {position[1]:.3f}, Z: {position[2]:.3f}")
                print(f"Rotation: Roll: {rotation[0]:.3f}, Pitch: {rotation[1]:.3f}, Yaw: {rotation[2]:.3f}")
                
                # Update GPS-like coordinates (This simulates a GPS feed using Vicon data)
                vehicle._location.global_frame.lat = position[0]  # Simulated latitude
                vehicle._location.global_frame.lon = position[1]  # Simulated longitude
                vehicle._location.global_frame.alt = position[2]  # Simulated altitude
                
                # Optionally, send this as MAVLink GPS_INPUT (more advanced)
                # vehicle.send_mavlink(...)

            time.sleep(0.1)  # Update every 100 ms
    except KeyboardInterrupt:
        print("Stopping...")
        vicon_client.disconnect()
        vehicle.close()

# Start updating drone position from Vicon data
update_vicon_position(vehicle)
