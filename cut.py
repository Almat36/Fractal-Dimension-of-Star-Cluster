import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

t = ["000057", "000114", "000285", "000570", "000855", "001140"]
for i in t:
    n=f"{i}"
    Data = np.genfromtxt(n+".den", usecols=(1,2,3))
    r = np.genfromtxt("def-dc 0.25.dat", usecols=(8))
    d0=[0,0,0]
    t = KDTree(Data)
    k = t.query_ball_point(d0, r[int(n)] )
    XYZ = Data[k]
    print(r[int(n)])
    np.savetxt(f"{i}_1xJR.txt",XYZ)

    # plt.figure(1)
    # plt.plot(Data[:,0],Data[:,1],"o")
    # plt.plot(XYZ[:,0],XYZ[:,1], "ro")
    
