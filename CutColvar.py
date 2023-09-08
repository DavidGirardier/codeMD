import numpy as np


inputfile = '500colvar_c60_precise_newdt0_2'
trajectories = np.loadtxt(inputfile)



alltime = []
alltraj = []
allvel = []
t = 20.0
newTime = 10.0

dtIni = 0.2
dtFinal = 0.2

numberTraj = 500
time = trajectories[:,0].reshape(numberTraj, int(t/dtIni)+1)
traj = trajectories[:,1].reshape(numberTraj, int(t/dtIni)+1)



alltime = alltime + [time[i,j] for i in range(numberTraj) for j in range(0, int(newTime/dtIni)+1,int(dtFinal/dtIni))]
alltraj = alltraj + [traj[i,j] for i in range(numberTraj) for j in range(0, int(newTime/dtIni)+1,int(dtFinal/dtIni))]

                

strdt=''
for l in str(dtFinal):
    
    if l == '.':
        strdt+='_'
    else:
        strdt+=l

outputName=inputfile + 'newt' + str(int(newTime)) + '_newdt' + strdt
print(outputName)

np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%1.8E')
print([max(alltraj),min(alltraj)])
np.savetxt(outputName+ 'qMinandMax', [max(alltraj),min(alltraj)], fmt='%1.8E')
