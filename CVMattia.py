import numpy as np
import matplotlib.pyplot as plt

for i in range(200):
    surf = np.loadtxt("SIZE/size."+str(i+1)+".dat")
    size = np.loadtxt("VOL/VOL."+str(i+1)+".dat")
    plt.plot(size, surf)




plt.xlabel('VOL')
plt.ylabel('surface')

plt.legend()
plt.show()