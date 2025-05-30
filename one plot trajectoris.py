import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Total number of markers
num_markers = len(labels)

# Define the grid size (e.g., square layout)
cols = 4  # adjust based on how many plots per row you want
rows = math.ceil(num_markers / cols)

# Create a figure with subplots
fig = plt.figure(figsize=(5 * cols, 5 * rows))  # scale figure size

for idx, label in enumerate(labels):
    marker_index = labels.index(label)
    x = marker_data[0, marker_index, :]
    y = marker_data[1, marker_index, :]
    z = marker_data[2, marker_index, :]

    ax = fig.add_subplot(rows, cols, idx + 1, projection='3d')
    ax.plot(x, y, z, label='Trajectory', color='orange')
    ax.set_title(f'{label}', fontsize=10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

plt.tight_layout()
plt.show()