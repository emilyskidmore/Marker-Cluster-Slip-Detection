import kineticstoolkit as ktk
import pandas as pd
import numpy as np
import ezc3d
import matplotlib.pyplot as plt

Nylon2 = ezc3d.c3d(r'C:\Users\milli\OneDrive - University of Strathclyde\Documents\Project\Python\Marker-Cluster-Slip-Detection\Kinetics Toolkit\Nylon2.c3d')

marker_data = Nylon2['data']['points']  
marker_data
marker_data = marker_data[:3, :, :]
marker_data = marker_data.transpose(2,1,0)

Marker_labels = Nylon2['parameters']['POINT']['LABELS']['value']
Marker_labels

# ===========================
# Creating Time Series of heel data
# ===========================

no_frames = marker_data.shape[0]
freq = Nylon2['header']['points']['frame_rate']
freq
duration = no_frames/ freq
duration 

ts_heel= ktk.TimeSeries()
ts_heel.time = np.arange(0, 120.9, 0.01)
ts_heel = ts_heel.add_data("RHEEL_X", marker_data[:,5,0])
ts_heel = ts_heel.add_data("RHEEL_Y", marker_data[:,4,1])
ts_heel = ts_heel.add_data("RHEEL_Z", marker_data[:,6,2])

# trying to identify local minima in y cooridnats to identify heel strike
heel_events = ktk.cycles.detect_cycles(ts_heel, data_key='RHEEL_Y')
heel_events.plot(["RHEEL_Y"])
plt.show()

# Idneitfying heel strike using scipy function
heel_y = ts_heel.data["RHEEL_Y"]
heel_y
inverse_heel_y = -ts_heel.data["RHEEL_Y"]
inverse_heel_y

from scipy.signal import find_peaks, find_peaks_cwt

peaks, properties = find_peaks(inverse_heel_y, distance=50, prominence=5)

time = ts_heel.time

plt.figure(figsize=(12, 4))
plt.plot(time, heel_y, label="Heel Y (vertical)")
plt.plot(time[peaks], heel_y[peaks], "rx", label="Detected Heel Strikes")
plt.xlabel("Time (s)")
plt.ylabel("Y Position (mm or m)")
plt.title("Heel Strike Detection (Local Minima of Heel Y)")
plt.legend()
plt.grid()
plt.show()

len(peaks)

# Cant seem to get around 109 peaks 
waveletpeaks = find_peaks_cwt(inverse_heel_y, widths=np.arange(30, 70))
plt.figure(figsize=(12, 4))
plt.plot(time, heel_y, label="Heel Y (vertical)")
plt.plot(time[waveletpeaks], heel_y[waveletpeaks], "rx", label="Detected Heel Strikes")
plt.xlabel("Time (s)")
plt.ylabel("Y Position (mm or m)")
plt.title("Heel Strike Detection (Local Minima of Heel Y)")
plt.legend()
plt.grid()
plt.show()
len(waveletpeaks)