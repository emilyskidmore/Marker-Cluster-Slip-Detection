import moveck_bridge_btk as btk

try:
    Read_Data = btk.btkReadAcquisition(r'C:\Users\kwb24166\OneDrive - University of Strathclyde\Documents\Project\Python\Data\run.c3d')
    print("Data loaded successfully")
    print(Read_Data)
except Exception as e:
    print("error:",e)

clusters = btk.btkGetPoints(Read_Data)
print(clusters)

point1 = btk.btkGetPoint(Read_Data, "LASIS")
print(point1)

#print(btk.__file__)

