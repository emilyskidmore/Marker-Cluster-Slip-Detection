'''
Creating 2D and 3D plots of all the marker trajectories. One method using the data fram creating in the 'Data into CSV' file 
and another using a method extracting the data directly from the c3d file. The dataframe has zeros put in where NA is the entry 
in the c3d file.
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# ============================================
# Plotting the x,y,z coordinates against frames on 3 subplots for one marker, using the dataframe
# ============================================

L_Thigh = 'LLTHI'
L_Thigh_data = df[df['Marker']== L_Thigh]

X = L_Thigh_data[['Frame','X']]
Y = L_Thigh_data[['Frame','Y']]
Z = L_Thigh_data[['Frame','Z']]

fig, axs = plt.subplots(nrows = 3, ncols=1, figsize=(10, 7.5), layout='constrained')
x_axis = X['Frame']
y_x = X['X']
y_y = Y['Y']
y_z = Z['Z']
axs[0].plot(x_axis, y_x)
axs[0].set_title('x-coordinate trajectory')

axs[1].plot(x_axis, y_y)
axs[1].set_title('y-coordinate trajectory')

axs[2].plot(x_axis, y_z)
axs[2].set_title('z coordinate trajectory')

plt.show()

# ============================================
# 3D plot of one marker
# ============================================
L_Thigh = 'LLTHI'
L_Thigh_data = df[df['Marker']== L_Thigh]

X = L_Thigh_data[['Frame','X']]
Y = L_Thigh_data[['Frame','Y']]
Z = L_Thigh_data[['Frame','Z']]

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
# Get the test data
x_axis = X['Frame']
y_x = X['X']
y_y = Y['Y']
y_z = Z['Z']

ax.plot(y_x, y_y,y_z, label = 'Marker Trajectory', color = 'orange')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Marker Trajectory - Left Thigh')
ax.legend()
plt.show()

# ============================================
# 3D trajectories of all markers - first Method using the dataframe 
# ============================================
df_markers = df['Marker']
print(df_markers)

# dimension of the figure given theres 28 markers
cols = 7  
rows = 4

# Create a figure with subplots
fig = plt.figure(figsize=(20,20))  

for i, marker in enumerate (df_markers):
    i_data = df[df['Marker'] == marker]
    x_data = i_data['X']
    y_data = i_data['Y']
    z_data = i_data['Z']
    
    ax = fig.add_subplot(rows, cols,i + 1, projection='3d')
    ax.plot(x_data, y_data, z_data, label='Trajectory', color='orange')
    ax.set_title(f'{marker}', fontsize=7)
    ax.set_xlabel('X', fontsize = 5 )
    ax.set_ylabel('Y', fontsize = 5)
    ax.set_zlabel('Z', fontsize = 5)


fig.tight_layout()
plt.savefig('Marker trajectories - df')
plt.show()

# ============================================
# 3D trajectories of all markers - Second Method using data directly from c3d file
# ============================================

marker_data = c3d['data']['points']  # shape: (4, N_markers, N_frames)
markers = c3d['parameters']['POINT']['LABELS']['value']

# dimension of the figure given theres 28 markers
cols = 7  
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
plt.savefig('Marker trajectories - c3d')
plt.show()

