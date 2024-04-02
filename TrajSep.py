import numpy as np


inputfile = 'colvar_c60_precise'
trajectories = np.loadtxt(inputfile)



alltimeA = []
alltrajA = []
alltimeB = []
alltrajB = []
allvel = []
t = 20.0


dtIni = 0.001
dtFinal = 0.01

numberTraj = 100

minA = 1.0
limit = 1.1
time = trajectories[:,0].reshape(numberTraj, int(t/dtIni)+1)
traj = trajectories[:,1].reshape(numberTraj, int(t/dtIni)+1)

counter = 0

# for k in traj:
#     for i in k:

#         if i<minA:
#             counter = counter + 1
#             alltime = np.concatenate([alltime,time[0]])
#             alltraj = np.concatenate([alltraj,k])
            
#             break

for k in traj:
    
    if k[-1]>1.2:
        counter = counter + 1
        alltimeB = np.concatenate([alltimeB,time[0]])
        alltrajB = np.concatenate([alltrajB,k])
    elif k[-1]< 1.1:
        alltimeA = np.concatenate([alltimeA,time[0]])
        alltrajA = np.concatenate([alltrajA,k])


# alltime = alltime + [time[i,j] for i in range(numberTraj) for j in range(0, len(time[0]),int(dtFinal/dtIni))]
# alltraj = alltraj + [traj[i,j] for i in range(numberTraj) for j in range(0, len(time[0]),int(dtFinal/dtIni))]

                


outputName=inputfile+'A'
print(outputName)

np.savetxt(outputName, np.c_[alltimeA,alltrajA], fmt='%1.8E')

outputName=inputfile+'B'
print(outputName)

np.savetxt(outputName, np.c_[alltimeB,alltrajB], fmt='%1.8E')
