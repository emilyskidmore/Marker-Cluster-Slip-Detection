import ezc3d
import pandas as pd
import numpy as np

# Load C3D
c3d = ezc3d.c3d('run.c3d')

# Extract marker data and labels
marker_data = c3d['data']['points']  # Shape: (4, num_markers, num_frames)
labels = c3d['parameters']['POINT']['LABELS']['value']

# Get only XYZ (ignore 4th row: camera residuals)
xyz_data = marker_data[:3, :, :]  # Shape: (3, num_markers, num_frames)

# Transpose and reshape to DataFrame
# Resulting shape will be (num_frames * num_markers, 5)
num_frames = xyz_data.shape[2]
num_markers = xyz_data.shape[1]

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