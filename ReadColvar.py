import numpy as np
from typing import List, TypeVar, Tuple, Dict, Set

inputfile = 'EulerFabiodt0_001.txt'
trajectories = np.loadtxt(inputfile)


alltime = []
alltraj = []
allvel = []
t = 1.0
dtIni = 0.001
dtFinal = 0.1
numberTraj = 500
time = trajectories[:,0].reshape(numberTraj, int(t/dtIni)+1)
traj = trajectories[:,1].reshape(numberTraj, int(t/dtIni)+1)
vel = trajectories[:,2].reshape(numberTraj, int(t/dtIni)+1)


alltime = alltime + [time[i,j] for i in range(numberTraj) for j in range(0, len(time[0]), int(dtFinal/dtIni))]
alltraj = alltraj + [traj[i,j] for i in range(numberTraj) for j in range(0, len(traj[0]), int(dtFinal/dtIni))]
allvel = allvel + [vel[i,j] for i in range(numberTraj) for j in range(0, len(vel[0]), int(dtFinal/dtIni))]

outputName='newdt.txt'
np.savetxt(outputName, np.c_[alltime,alltraj,allvel], fmt='%1.8E')

