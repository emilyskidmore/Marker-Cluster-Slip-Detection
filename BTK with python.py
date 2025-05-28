#Trying to use BTK to read cd3 running file
# pip install moveck-bridge-btk - type into terminal to install package
#Importing the BTK package
import moveck_bridge_btk as btk

# Check the available functions and classes int he btk package
print(dir(btk))


try:
    Read_Data = btk.btkReadAcquisition(r'C:\Users\milli\OneDrive - University of Strathclyde\Documents\Project\Python\Data')
    print("Data loaded successfully")
    print(Read_Data)
except Exception as e:
    print("error:",e)



Marker_Data = btk.btkGetMarkers(Read_Data)
print("Markers", Marker_Data)
#print(Marker_Data, [1,1])

time_0 = btk.btkGetFirstFrame(Read_Data)
print(time_0)
time_t = btk.btkGetLastFrame(Read_Data)
print(time_t)

no_frames = btk.btkGetPointFrameNumber(Read_Data)
print(f"Number of frames - {no_frames}")
no_data_points = btk.btkGetPointNumber(Read_Data)
print(no_data_points)
frame_freq = btk.btkGetPointFrequency(Read_Data)
print(f"Point frequency - {frame_freq}")
Duration = no_frames/ frame_freq
print(f"Run duration - {Duration} seconds")


