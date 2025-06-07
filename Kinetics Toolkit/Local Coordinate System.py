import kineticstoolkit as ktk
import pandas as pd
import numpy as np
import ezc3d
import matplotlib.pyplot as plt

'''
Nylon2 = ktk.read_c3d(r'C:\Users\milli\OneDrive - University of Strathclyde\Documents\Project\Python\Marker-Cluster-Slip-Detection\Kinetics Toolkit\Nylon2.c3d', convert_point_unit=False)
markers = Nylon2["Points"]
print(markers.data.keys())
'''

Nylon2 = ezc3d.c3d(r'C:\Users\milli\OneDrive - University of Strathclyde\Documents\Project\Python\Marker-Cluster-Slip-Detection\Kinetics Toolkit\Nylon2.c3d')

marker_data = Nylon2['data']['points']  
marker_data
marker_data = marker_data[:3, :, :]
marker_data
marker_data = marker_data.transpose(2,1,0)
marker_data
Marker_labels = Nylon2['parameters']['POINT']['LABELS']['value']

# ===========================
# Creating Time Series
# ===========================

no_frames = marker_data.shape[0]
freq = Nylon2['header']['points']['frame_rate']
freq
duration = no_frames/ freq
duration 

Marker_labels
marker_data[:,4,:] # RThiClust 2

ts = ktk.TimeSeries()
ts.time = np.arange(0, 120.9, 0.01)
ts = ts.add_data("RThiClust1", marker_data[:,5,:])
ts = ts.add_data("RThiClust2", marker_data[:,4,:])
ts = ts.add_data("RThiClust3", marker_data[:,6,:])
ts.data

 
# ===========================
# Creating local Coordinate system at t=0
# ===========================

# STEP 1 - Define x axis
# Arbitarily choose marker RThiClust1 as the origin
origin = marker_data[0,5,:]
origin
# Calculating distance between RThiClust1 and RThiClust2
marker1_2 = marker_data[0,4,:] - origin
# Magnitude of vector RThiClust1 to RThiClust2 = marker1_2
distance1_2 = np.linalg.norm(marker1_2)
distance1_2 

# Calculating distance between RThiClust1 and RThiClust3
marker1_3 = marker_data[0,6,:] - origin
distance1_3 = np.linalg.norm(marker1_3)
distance1_3
# Distance from 1 to 2 is smaller than the distance from 1 to 3, so choose the vector 1 to 3 to be the x axis
x_axis =  marker1_3/np.linalg.norm(marker1_3)
x_axis 

# STEP 2 - Define a support axis to define the plane orientation 
y_temp = marker1_2 / np.linalg.norm(marker1_2)

# STEP 3 - Define a second axis perpendicular to the plane, this ensures the z axis is perepndicualr to the plane containing x_axis and y_temp
z = np.cross(y_temp, x_axis)
z_axis = z/np.linalg.norm(z)
z_axis
mag_z = np.linalg.norm(z_axis)
mag_z

# STEP 4 - orthogonalise the system 
y = np.cross(z_axis,x_axis)
y_axis = y/np.linalg.norm(y)
y_axis
mag_y = np.linalg.norm(y_axis)
mag_y

# STEP 5 - construct the orientation matrix
R0 = np.array((x_axis, y_axis, z_axis))

# From kinetics toolkit a transform always has the form 4x4 where the top left 3x3 is the rotation matrix 
# and the last column is the position of the local coordinate system's origin,
# [R11 R12 R13 Ox]
# [R21 R22 R23 Oy]
# [R31 R32 R33 Oz]
# [ 0   0   0   1]
'''
T = np.array((x_axis, y_axis, z_axis, origin))
T = np.transpose(T)
extra_row = [0,0,0,1]
T = np.append(T, extra_row)
T
'''

# ===========================
# Tracking cluster movement over the time series
# ===========================

R_all = np.zeros((no_frames, 3, 3))
t_all = np.zeros((no_frames, 3))

for i in range(no_frames):
    origin_i = marker_data[i,5,:]
    marker1_2_i = marker_data[i,4,:] - origin_i
    marker1_3_i = marker_data[i,6,:] - origin_i

    xax_i = marker1_3_i/np.linalg.norm(marker1_3_i)
    y_temp_i = marker1_2_i / np.linalg.norm(marker1_2_i)
    z_i = np.cross(y_temp_i, xax_i)
    zax_i = z_i/np.linalg.norm(z_i)
    y_i = np.cross(zax_i, xax_i)
    yax_i = y_i/np.linalg.norm(y_i)

    R_i = np.vstack((xax_i, yax_i, zax_i))

    R_rel = R0 @ R_i.T
    t_rel = R0 @ (origin_i - origin)

    R_all[i] = R_rel
    t_all[i] = t_rel

