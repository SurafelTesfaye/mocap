#Test script from inside this folder
#C:\Users\OEM\AppData\Local\Programs\Python\Python38\lib\site-packages\vicon_dssdk

from ViconDataStream import Client, DataStreamException
import time

# Initialize Vicon client
client = Client()

# Connect to Vicon DataStream
client.Connect("localhost:801")  # Replace "localhost" with your Vicon server's IP if it's remote

# Enable data types
client.EnableSegmentData()

# Set the stream mode to EClientPull for manual frame pulling
client.SetStreamMode(Client.StreamMode.EClientPull)

# Loop to continuously print position and orientation
while True:
    try:
        # Get the latest frame of data
        client.GetFrame()

        # Use the name of your object "USL500"
        segment_name = "USL500"
        translation, translation_valid = client.GetSegmentGlobalTranslation(segment_name, segment_name)
        orientation, orientation_valid = client.GetSegmentGlobalRotationQuaternion(segment_name, segment_name)

        # Log time for reference
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"Time: {current_time}")

        # Check if the data is valid before printing
        if translation_valid:
            x, y, z = translation
            print(f"Position: X={x:.2f}, Y={y:.2f}, Z={z:.2f}")
        else:
            print("Translation data is invalid.")

        if orientation_valid:
            w, qx, qy, qz = orientation
            print(f"Orientation (Quaternion): W={w:.4f}, X={qx:.4f}, Y={qy:.4f}, Z={qz:.4f}")
        else:
            print("Orientation data is invalid.")

        print()  # Blank line for readability

    except DataStreamException as e:
        print(f"Error: {str(e)}")

    # Pause briefly to prevent overwhelming the output
    time.sleep(1)
