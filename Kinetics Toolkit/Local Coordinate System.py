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

