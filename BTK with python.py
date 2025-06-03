#Trying to use BTK to read cd3 running file
# pip install moveck-bridge-btk - type into terminal to install package
#Importing the BTK package
import moveck_bridge_btk as btk
import numpy as np
import sys

# Check the available functions and classes int he btk package
print(dir(btk))

data = btk.btkReadAcquisition('run.c3d')
#print(data)


Marker_Data = btk.btkGetMarkers(data)
print({len(Marker_Data)})
print(type(Marker_Data))
print(type(Marker_Data[0]))
print(Marker_Data)

time_0 = btk.btkGetFirstFrame(data)
print(time_0)
time_t = btk.btkGetLastFrame(data)
print(time_t)

no_frames = btk.btkGetPointFrameNumber(data)
print(f"Number of frames - {no_frames}")
no_data_points = btk.btkGetPointNumber(data)
print(no_data_points)
frame_freq = btk.btkGetPointFrequency(data)
print(f"Point frequency - {frame_freq}")
Duration = no_frames/ frame_freq
print(f"Run duration - {Duration} seconds")



