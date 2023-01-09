from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt

trajectories = np.loadtxt('Freeparticle_t1_dt0_01_g10_m1')
numberBins = 180
minPos = -1.8
maxPos = 1.8
sizeBin = (maxPos - minPos)/numberBins
counter = 0
arrayBins = np.zeros((numberBins,2))
y = np.zeros(numberBins)
x = np.zeros(numberBins)
for k in range(np.size(arrayBins,0)):
    arrayBins[k][0] = k*sizeBin + minPos



for i in range(np.size(trajectories, 0)):
    counter += 1 
    #print(trajectories[i][1])
    associatedBin = int((trajectories[i][1] + minPos)/sizeBin)
    arrayBins[associatedBin][1] += 1

for k in range(np.size(arrayBins,0)):
    
    y[k] = arrayBins[k][1]/counter
    x[k] = arrayBins[k][0]
    #print(str(x[k])+'\t'+str(y[k]))



# plt.plot(x,y)
# plt.plot(x,-np.log(y))
# plt.show()
#np.savetxt('FEfromRho', np.c_[x,-np.log(y),y], header='# x F rho')

x_final = [trajectories[i-1][1] for i in range(101,len(trajectories)+1, 101)]
v_final = [trajectories[i-1][2] for i in range(101,len(trajectories)+1, 101)]
print(np.var(x_final))
print(np.var(v_final))
np.savetxt('FEfromRhoCicotti', np.c_[x,y], header='# x rho')
