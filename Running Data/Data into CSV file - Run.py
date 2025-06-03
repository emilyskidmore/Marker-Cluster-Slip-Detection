'''
Taking run.c3d c3d data and creating a dataframe from it which is then exported into a csv file which can be opened in excel
'''

import ezc3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import moveck_bridge_btk as btk

# Load C3D
c3d = ezc3d.c3d('run.c3d')

# Extract marker data in the form of a numpy array that contains the marker coordinates
# The following extracts the marker positions ['points'] from the numerical data ['data'] of the file
marker_data = c3d['data']['points']  # Shape: (4, num_markers, num_frames)
# Finding the shape of the numpy array - typically it is (4, no.markers, no.frames)
# The first dimension is often 4 [x,y,z,residual]
marker_data.shape 
print(f"The data has the shape {marker_data.shape} which means it contains x,y,z coordinates and a residual, {marker_data.shape[1]} markers and {marker_data.shape[2]} frames")
# The following accesses the parameters section of the c3d file, then into 'point' which contains information about the markers, then into 'labels' which is the names of the markers used, then finally into 'values' which is a string of the marker labels
Marker_labels = c3d['parameters']['POINT']['LABELS']['value']


# Get only x,y,z coordinates, ignoring the residual
marker_data = marker_data[:3, :, :]  # Shape: (3, num_markers, num_frames)
print(f"The data has the shape {marker_data.shape} which means it contains x,y,z coordinates, {marker_data.shape[1]} markers and {marker_data.shape[2]} frames")

no_frames = marker_data.shape[2]
no_markers = marker_data.shape[1]
print(f"The number of markers is {no_markers}")
print(f"The number of frames is {no_frames}")

# Create a DataFrame
# Creating an empty list to append items to
dataframe = []
# Looping over the total number of frames
for i in range(no_frames):
    # Loopig over each marker label for each frame and appending the data to the list
    for j, label in enumerate(Marker_labels):
        x, y, z = marker_data[:, j, i]
        dataframe.append({
            'Frame': i,
            'Marker': label,
            'X': x,
            'Y': y,
            'Z': z
        })

# Turning the list into a data frame
df = pd.DataFrame.from_records(dataframe)
# Turning any empty entries into 0s
df = df.fillna(0) 
# Turning the list into a csv file
df.to_csv("Data - Run.csv")