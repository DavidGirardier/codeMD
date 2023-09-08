import numpy as np

numberOfFile = 500
tFile = 1.0
dt = 0.001
nLine = int(tFile/dt +1)

inputfile = 'Freeparticle_t1_dt0_001_g10_m1'
positionAndvelocities = []



for j in range(numberOfFile):
    
    
    trajectory = np.loadtxt(inputfile, skiprows=nLine*j, max_rows=nLine) 
    print(trajectory)
    
    
    for k in range(0,len(trajectory)):

        if k == 0:

            velocity = (trajectory[k+1][1]-trajectory[k][1])/dt
            
        elif k == len(trajectory)-1:

            velocity = (trajectory[k][1]-trajectory[k-1][1])/dt

        else :
            velocity = (trajectory[k+1][1]-trajectory[k-1][1])/(2.0*dt)


        #print(velocity)
        #velocity = (trajectory[k+1][1]-trajectory[k][1])/(dt)

        positionAndvelocities.append([trajectory[k][0],trajectory[k][1], velocity])
    print('traj' + str(j) + 'done')
    
#print(positionAndvelocities)
v = []
v2 = []
myMean=0.0
for i in range(np.size(positionAndvelocities,0)):
    v.append(positionAndvelocities[i][2])
    v2.append(positionAndvelocities[i][2]*positionAndvelocities[i][2]) 
    myMean += positionAndvelocities[i][2]*positionAndvelocities[i][2]

print('m = ' + str(str(1./np.mean(v2))))
print('<v^2> = ' + str(np.mean(v2)))
print('<v> = ' + str(np.mean(v)))

outputName = inputfile + '_vel'
np.savetxt(outputName, np.c_[positionAndvelocities], fmt='%1.6E')

