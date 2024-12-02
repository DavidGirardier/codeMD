import numpy as np


inputfile = input('file:')
trajectories = np.loadtxt(inputfile)

IsVel = False

alltime = []
alltraj = []
allvel = []
t = 2000.
dtIni = 0.002


dtList = [0.8]
for dtime in dtList :
    alltime = []
    alltraj = []
    allvel = []

    dtFinal = dtime
    
    

    alltime = alltime + [trajectories[j,0]  for j in range(0, len(trajectories[:,0]), int(dtFinal/dtIni))]
    alltraj = alltraj + [trajectories[j,1]  for j in range(0, len(trajectories[:,0]), int(dtFinal/dtIni))]
    
    

    outputName=inputfile + '_newdt' + str(dtime)

    if IsVel == True :
        np.savetxt(outputName, np.c_[alltime,alltraj,allvel], fmt='%1.8E')
    else:
        np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%1.8E')
    print(outputName)
    print([max(alltraj),min(alltraj)])
    np.savetxt(outputName+ 'qMinandMax', [max(alltraj),min(alltraj)], fmt='%1.8E')
    np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%1.8E')

    

