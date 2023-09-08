import numpy as np


inputfile = 'colvar_d_c60'
trajectories = np.loadtxt(inputfile)



alltime = []
alltraj = []
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
    for i in k:

        if i<limit:
            
            break
        if i == k[-1]:
            counter = counter + 1
            alltime = np.concatenate([alltime,time[0]])
            alltraj = np.concatenate([alltraj,k])


# alltime = alltime + [time[i,j] for i in range(numberTraj) for j in range(0, len(time[0]),int(dtFinal/dtIni))]
# alltraj = alltraj + [traj[i,j] for i in range(numberTraj) for j in range(0, len(time[0]),int(dtFinal/dtIni))]
print(counter)
                


outputName=inputfile+'NoA'
print(outputName)

np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%1.8E')
print([max(alltraj),min(alltraj)])
np.savetxt(outputName+ 'qMinandMax', [max(alltraj),min(alltraj)], fmt='%1.8E')
