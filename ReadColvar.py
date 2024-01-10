import numpy as np


inputfile = '500traj2ps'
trajectories = np.loadtxt(inputfile)

IsVel = False

alltime = []
alltraj = []
allvel = []
t = 1.9999
dtIni = 0.0001
dtFinal = 0.001
numberTraj = 500
time = trajectories[:,0].reshape(numberTraj, int(t/dtIni)+1)
traj = trajectories[:,1].reshape(numberTraj, int(t/dtIni)+1)
if IsVel == True :
    vel = trajectories[:,2].reshape(numberTraj, int(t/dtIni)+1)


alltime = alltime + [time[i,j] for i in range(numberTraj) for j in range(0, len(time[0]), int(dtFinal/dtIni))]
alltraj = alltraj + [traj[i,j] for i in range(numberTraj) for j in range(0, len(traj[0]), int(dtFinal/dtIni))]
if IsVel == True :
    allvel = allvel + [vel[i,j] for i in range(numberTraj) for j in range(0, len(traj[0]), int(dtFinal/dtIni))]
# if IsVel == True :
#     # allvel = allvel + [vel[i,j] for i in range(numberTraj) for j in range(0, len(vel[0]), int(dtFinal/dtIni))]
#     for i in range(numberTraj):
#         for j in range(0, len(vel[0]), int(dtFinal/dtIni)):
#             sumVel = 0

            
#             for k in range(int(dtFinal/dtIni)):
#                 if j !=len(vel[0])-1:
#                     sumVel += vel[i,j+k]
#                     print(vel[i,j+k])
#                 else:
#                     sumVel += vel[i,j-k]
            
#             allvel = allvel + [sumVel/(int(dtFinal/dtIni))]
#             print(allvel)
#             exit()
                

strdt=''
for l in str(dtFinal):
    
    if l == '.':
        strdt+='_'
    else:
        strdt+=l

outputName=inputfile + '_newdt' + strdt

if IsVel == True :
    np.savetxt(outputName, np.c_[alltime,alltraj,allvel], fmt='%1.8E')
else:
    np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%1.8E')
print(outputName)
print([max(alltraj),min(alltraj)])
np.savetxt(outputName+ 'qMinandMax', [max(alltraj),min(alltraj)], fmt='%1.8E')
