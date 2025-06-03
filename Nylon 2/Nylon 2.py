'''
Taking Nylon2.c3d c3d data and creating a dataframe from it which is then exported into a csv file which can be opened in excel.
Plotting the marker trajectories for the 12 markers in the Nylon2 data frame.
'''

import ezc3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import moveck_bridge_btk as btk

# ============================================
# Creating Dataframe  
# ============================================

# Load C3D
c3d = ezc3d.c3d(r'C:\Users\milli\OneDrive - University of Strathclyde\Documents\Project\Python\Marker-Cluster-Slip-Detection\Nylon 2\Nylon2.c3d')

# Extract marker data in the form of a numpy array that contains the marker coordinates
# The following extracts the marker positions ['points'] from the numerical data ['data'] of the file
marker_data = c3d['data']['points']  # Shape: (4, num_markers, num_frames)
# Finding the shape of the numpy array - typically it is (4, no.markers, no.frames)
# The first dimension is often 4 [x,y,z,residual]
marker_data.shape 
print(f"The data has the shape {marker_data.shape} which means it contains x,y,z coordinates and a residual, {marker_data.shape[1]} markers and {marker_data.shape[2]} frames")
# The following accesses the parameters section of the c3d file, then into 'point' which contains information about the markers, then into 'labels' which is the names of the markers used, then finally into 'values' which is a string of the marker labels
Marker_labels = c3d['parameters']['POINT']['LABELS']['value']
print(Marker_labels)

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
# Turning any empty entries into 0s - not necessary the only entries that have blanks are labels 10 and 11 which are not required.
# df = df.fillna(0) 
# Turning the list into a csv file
df.to_csv("Nylon 2/ Data- Nylon2.csv", index=False)

# ============================================
# 3D trajectories of all markers - second Method using the c3d data directly
# ============================================

marker_data = c3d['data']['points']  # shape: (4, N_markers, N_frames)
markers = c3d['parameters']['POINT']['LABELS']['value']

# dimension of the figure given theres 28 markers
cols = 3  
rows = 4

# Create a figure with subplots
fig = plt.figure(figsize=(20,20))  

for i, marker in enumerate(markers):
    marker_index = markers.index(marker)
    x = marker_data[0, marker_index, :]
    y = marker_data[1, marker_index, :]
    z = marker_data[2, marker_index, :]

    ax = fig.add_subplot(rows, cols,i + 1, projection='3d')
    ax.plot(x, y, z, label='Trajectory', color='orange')
    ax.set_title(f'{marker}', fontsize=7)
    ax.set_xlabel('X', fontsize = 5 )
    ax.set_ylabel('Y', fontsize = 5)
    ax.set_zlabel('Z', fontsize = 5)

fig.tight_layout()
plt.savefig('Nylon 2/Marker trajectories - c3d Nylon.png')
plt.show()

# ============================================
# Plotting the x,y,z coordinates against frames on 3 subplots for one marker, using the dataframe
# ============================================

markers = df['Marker'].unique() 


for i in markers:
    Marker_data = df[df['Marker'] == i]
    x = Marker_data['X']
    y = Marker_data['Y']
    z = Marker_data['Z']
    frames = Marker_data['Frame']

    fig, axs = plt.subplots(nrows = 3, ncols=1, figsize=(10, 7.5), sharex=True)

    axs[0].plot(frames, x)
    axs[0].set_title('x-coordinate trajectory')
    axs[1].plot(frames, y)
    axs[1].set_title('y-coordinate trajectory')
    axs[2].plot(frames, z)
    axs[2].set_title('z coordinate trajectory') 
    axs[2].set_xlabel('Frame')
    
    plt.suptitle(f'Trajectory of Marker: {i}', fontsize=12)
    plt.tight_layout()
plt.show()

