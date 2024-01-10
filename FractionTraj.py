import numpy as np
inputfile = '500traj2ps_newdt0_001'
trajectories = np.loadtxt(inputfile)

fractions = 5
x = []
y = []
z = []
size = int(np.size(trajectories, 0)/fractions)
for i in range(fractions):
    for j in range(i*size, (i+1)*size):
        x.append(trajectories[j][0])
        y.append(trajectories[j][1])
        #z.append(trajectories[j][2])
    
    outputName = 'fraction' + inputfile + '_' + str(i+1)
    print(outputName)
    #np.savetxt(outputName, np.c_[x,y,z], fmt='%1.8E')
    np.savetxt(outputName, np.c_[x,y], fmt='%1.8E')
    x = []
    y = []
    z = []

