import numpy as np


inputfile = 'TrajDW5_Gnct_M1_dt0_0001_t10'
trajectories = np.loadtxt(inputfile)


alltime = []
alltraj = []
allvel = []
t = 10.0
dtIni = 0.0001
dtFinal = 0.001
numberTraj = 100
time = trajectories[:,0].reshape(numberTraj, int(t/dtIni)+1)
traj = trajectories[:,1].reshape(numberTraj, int(t/dtIni)+1)
vel = trajectories[:,2].reshape(numberTraj, int(t/dtIni)+1)


alltime = alltime + [time[i,j] for i in range(numberTraj) for j in range(0, len(time[0]), int(dtFinal/dtIni))]
alltraj = alltraj + [traj[i,j] for i in range(numberTraj) for j in range(0, len(traj[0]), int(dtFinal/dtIni))]
allvel = allvel + [vel[i,j] for i in range(numberTraj) for j in range(0, len(vel[0]), int(dtFinal/dtIni))]

outputName=inputfile + '_newdt'
np.savetxt(outputName, np.c_[alltime,alltraj,allvel], fmt='%1.8E')

