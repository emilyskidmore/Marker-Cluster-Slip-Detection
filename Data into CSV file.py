import ezc3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import moveck_bridge_btk as btk


# Load data from cd3 file
c3d = ezc3d.c3d('run.c3d')

# Extract marker data in the form of a numpy array that contains the marker coordinates
# The following extracts the marker positions ['points'] from the numerical data ['data'] of the file 
marker_data = c3d['data']['points']
# Finding the shape of the numpy array - typically it is (4, no.markers, no.frames)
# The first dimension is often 4 [x,y,z,residual]
marker_data.shape 
print(f"The data has the shape {marker_data.shape} which means it contains x,y,z coordinates and a residual, {marker_data.shape[1]} markers and {marker_data.shape[2]} frames")
# The following accesses the parameters section of the c3d file, then into 'point' which contains information about the markers, then into 'labels' which is the names of the markers used, then finally into 'values' which is a string of the marker labels
Marker_labels = c3d['parameters']['POINT']['LABELS']
print(Marker_labels)

# Get only x,y,z coordinates, ignoring the residual
marker_data = marker_data[:3, :, :]  # The shape becomes (3,no.markers, no.frames)
print(f"The data has the shape {marker_data.shape} which means it contains x,y,z coordinates, {marker_data.shape[1]} markers and {marker_data.shape[2]} frames")
no_markers = marker_data.shape[1]
no_frames = marker_data.shape[2]
print(f"The number of markers is {no_markers}")
print(f"The number of frames is {no_frames}")

# Create a DataFrame
records = []
for frame_idx in range(num_frames):
    for marker_idx, label in enumerate(labels):
        x, y, z = xyz_data[:, marker_idx, frame_idx]
        records.append({
            'Frame': frame_idx,
            'Marker': label,
            'X': x,
            'Y': y,
            'Z': z
        })

df = pd.DataFrame.from_records(records)
df.to_csv("Data.csv")
print(labels)

L_Thigh = 'LLTHI'
L_Thigh_data = df[df['Marker']== L_Thigh]
print(L_Thigh_data)

X = L_Thigh_data['X']
Y = L_Thigh_data['Y']
Z = L_Thigh_data['Z']
print(X)
print(Y)
print(Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='2d')
ax.plot3D(marker_df['X'], marker_df['Y'], marker_df['Z'], label='LLTHI', color='blue')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f"Trajectory of Marker: {L_Thigh}")
ax.legend()
plt.show()