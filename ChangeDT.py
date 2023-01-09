import numpy as np
#inputfile = input("File: ")
inputfile = '500TrajFgmx2dt0_001t10'
trajectories = np.loadtxt(inputfile)
resolutionFactor = 10
x = []
y = []
z = []


for j in range(0,len(trajectories)):
    if j%10 == 0 :
    
        x.append(trajectories[j][0])
        y.append(trajectories[j][1])
        z.append(trajectories[j][2])

outputName = inputfile + '_newDT'
np.savetxt(outputName, np.c_[x,y,z])


