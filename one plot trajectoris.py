import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

marker_data = c3d['data']['points']  # shape: (4, N_markers, N_frames)
markers = c3d['parameters']['POINT']['LABELS']['value']
print(markers)
print(len(markers))

# dimension of the figure given theres 28 markers
cols = 7  
rows = 4

# Create a figure with subplots
fig = plt.figure(figsize=(30,30))  

for i, marker in enumerate(markers):
    marker_index = markers.index(marker)
    x = marker_data[0, marker_index, :]
    y = marker_data[1, marker_index, :]
    z = marker_data[2, marker_index, :]

    ax = fig.add_subplot(rows, cols,i + 1, projection='3d')
    ax.plot(x, y, z, label='Trajectory', color='orange')
    ax.set_title(f'{marker}', fontsize=7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

fig.tight_layout()
plt.show()