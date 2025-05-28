import moveck_bridge_btk as btk
import numpy as np

print(dir(btk))

data = btk.btkReadAcquisition('run.c3d')
#print(data)

no_frames = btk.btkGetPointFrameNumber(data)
print(f"Number of frames - {no_frames}")
no_data_points = btk.btkGetPointNumber(data)
print(no_data_points)
frame_freq = btk.btkGetPointFrequency(data)
print(f"Point frequency - {frame_freq}")
Duration = no_frames/ frame_freq
print(f"Run duration - {Duration} seconds")


Marker_Data = btk.btkGetMarkers(data)
print({len(Marker_Data)})
print(type(Marker_Data))
print(type(Marker_Data[0]))

# frequency = 100, so motion capture was recorded at 100Hz
# units indicated are mm
# Array shape indicates (2969, 3) - 2969 frames and x,y,z coordinates in mm
print(Marker_Data)
Marker_names = list(Marker_Data.keys())



time_0 = btk.btkGetFirstFrame(data)
print(time_0)
time_t = btk.btkGetLastFrame(data)
print(time_t)

values = btk.btkGetPointsValues(data)
print(values)
rows,cols = values.shape
# Rows is the number of frames
# Columns is the number of extracted points x 3? for the x,y,z components, so 28 points
print(f"Rows - {rows}, Columns - {cols}")
# printing the first row and all columns which gives 84 values 
print(values[0,:])