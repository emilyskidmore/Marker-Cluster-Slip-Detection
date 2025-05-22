#Trying to use BTK to read cd3 running file

#Importing the BTK package
import moveck_bridge_btk as btk

# Check the available functions and classes int he btk package
print(dir(btk))

#reader = btk.btkReadAcquisition(r'C:\Users\kwb24166\OneDrive - University of Strathclyde\Documents\Project\Python\Data\run.c3d')

try:
    acquisition = btk.btkReadAcquisition(r'C:\Users\kwb24166\OneDrive - University of Strathclyde\Documents\Project\Python\Data\run.c3d')
    print("acquisition data loaded successfully")
    print(acquisition)
except Exception as e:
    print("error:",e)

markers = btk.btkGetMarkers(acquisition)
print("Markers", markers)