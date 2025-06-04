import kineticstoolkit as ktk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.ion
#plt.ioff

Nylon2 = ktk.read_c3d(r'C:\Users\milli\OneDrive - University of Strathclyde\Documents\Project\Python\Marker-Cluster-Slip-Detection\Kinetics Toolkit\Nylon2.c3d', convert_point_unit=False)

Nylon2["Points"].data
Nylon2["Analogs"].data

markers = Nylon2["Points"]
p = ktk.Player(markers)
p.play()
p.up = "z"
p.anterior = "-y"
p.set_view("right")
p.interconnections["RThighCluster"] = {"Links" : [["RThiClust2", "RThiClust3", "RThiClust1", "RThiClust2"]], "Color": "b"}
p.interconnections["RLegCluster"] = {"Links" : [["RLegClust1", "RLegClust2", "RLegClust3", "RLegClust1"]], "Color" : "r"}
p.interconnections["RFoot"] = {"Links" : [["RANK", "RTOE", "RHEE", "RANK"]], "Color" : "g"}
plt.show()
