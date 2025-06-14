import ezc3d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import moveck_bridge_btk as btk

# Load C3D
c3d = ezc3d.c3d('run.c3d')

#See highets level gorups
print(c3d.keys())  

# See all parameter groups
print(c3d['parameters'].keys())  

print(c3d['header'].keys())
print(c3d['data'].keys())

# See all items in the 'POINT' group - within 'parameters'
print(c3d['parameters']['POINT'].keys())  # Example: 'LABELS', 'RATE', 'UNITS', etc.
print(c3d['parameters']['ANALOG'].keys())

# Print all point labels (marker names)
print(c3d['parameters']['POINT']['LABELS'])
print(c3d['parameters']['POINT']['LABELS']['value'])


# Access the actual 3D point data (shape: 4 x #points x #frames)
marker_data = c3d['data']['points']
print(marker_data.shape)