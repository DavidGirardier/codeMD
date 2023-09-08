import numpy as np


inputfile = '40Asso5ns'
trajectories = np.loadtxt(inputfile)



alltime = []
alltraj = []
allvel = []
t = 5000.0


dt = 0.01
tinterval = 200
twell = 20

numberTraj = 40
time = trajectories[:,0].reshape(numberTraj, int(t/dt)+1)
traj = trajectories[:,1].reshape(numberTraj, int(t/dt)+1)

reactiveTraj = []
reactiveTime = []

for i in range(len(traj[:,1])):
    for j in range(len(traj[0])):
        
        if traj[i,j] < 1.0 :
            
            reactiveTraj.extend(traj[i,j-int(tinterval/dt):j+int(twell/dt+1)])
            reactiveTime.extend([x*dt for x in range(int((tinterval+twell)/dt+1))])
            break



outputName=inputfile + 'react_t' + str(int(tinterval+twell))
print(outputName)

np.savetxt(outputName, np.c_[reactiveTime,reactiveTraj], fmt='%1.8E')

