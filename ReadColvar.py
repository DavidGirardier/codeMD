import numpy as np


inputfile = '100shortZWall_sd0_01'
trajectories = np.loadtxt(inputfile)

IsVel = False
fractions = 5
alltime = []
alltraj = []
allvel = []
t = 5.
dtIni = 0.002
numberTraj = 100
#dtList = [0.005,0.01,0.02,0.05,0.1]

dtList = [0.01]
for dtime in dtList :
    alltime = []
    alltraj = []
    allvel = []

    dtFinal = dtime
    
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
                    

    # strdt=''
    # for l in str(dtFinal):
        
    #     if l == '.':
    #         strdt+='_'
    #     else:
    #         strdt+=l

    outputName=inputfile + '_newdt' + str(dtime)

    if IsVel == True :
        np.savetxt(outputName, np.c_[alltime,alltraj,allvel], fmt='%1.8E')
    else:
        np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%1.8E')
    print(outputName)
    print([max(alltraj),min(alltraj)])
    np.savetxt(outputName+ 'qMinandMax', [max(alltraj),min(alltraj)], fmt='%1.8E')

    
    x = []
    y = []
    z = []
    size = int(np.size(alltraj, 0)/fractions)
    for i in range(fractions):
        for j in range(i*size, (i+1)*size):
            x.append(alltime[j])
            y.append(alltraj[j])
            #z.append(trajectories[j][2])
        
        outputNameFinal = 'fraction' + outputName + '_' + str(i+1)
        print(outputNameFinal)
        #np.savetxt(outputName, np.c_[x,y,z], fmt='%1.8E')
        np.savetxt(outputNameFinal, np.c_[x,y], fmt='%1.8E')
        x = []
        y = []
        z = []
