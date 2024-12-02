import numpy as np

from scipy.fftpack import fft, ifft, ifftshift

import matplotlib.pyplot as plt
import math




inputfile= 'fractionlightOWHeavyC_10ns_well_newdt0.1_1'
inputprof= 'FEfromRho_lightOWHeavyC_10ns_well'

unzoomedFactor = 1

trajectory = np.loadtxt(inputfile, skiprows=0, max_rows=10)
dt = trajectory[1,0]-trajectory[0,0]
print(dt)
m = 1555
kT = 1.0
gamma = 0.0

#dt=0.001
numberOfTraj = 1
tFile = 1000
nLine = tFile/dt
newdt = dt * unzoomedFactor

matrixXAC = []
matrixVAC = []

for i in range(numberOfTraj):
    trajectory = np.loadtxt(inputfile, skiprows=int(nLine)*i, max_rows=int(nLine)+1)
    
    unzoomedPos = [x for x in trajectory]
    
    #unzoomedPos2 = trajectory[unzoomedFactor:unzoomedFactor:-unzoomedFactor,1]
    #print(unzoomedPos2)
    unzoomedVel = [(trajectory[i+1*unzoomedFactor,1]-trajectory[i-1*unzoomedFactor,1])/(2.*dt*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    unzoomedVel = np.array(unzoomedVel)

    unzoomedAcc = [(trajectory[i+1*unzoomedFactor,1]-2.*trajectory[i,1]+trajectory[i-1*unzoomedFactor,1])/(dt*dt*unzoomedFactor*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    unzoomedAcc2 = [(unzoomedVel[i+1*unzoomedFactor]-unzoomedVel[i-1*unzoomedFactor])/(2.0*dt*unzoomedFactor) for i in range(1*unzoomedFactor,len(unzoomedVel)-1*unzoomedFactor,unzoomedFactor)]
    #realAcc = [a for a in trajectory[:,3]]
    realAcc = np.zeros(len(unzoomedVel))
    
    unzoomedAcc = np.array(unzoomedAcc)
    unzoomedPos = np.array(unzoomedPos)
    unzoomedAcc2 = np.array(unzoomedAcc2)
    realAcc = np.array(realAcc)
    
    
    profile = np.loadtxt(inputprof)
    
    pos = profile[:,0]
    pos_min = profile[0,0]
    dpos = profile[1,0]-profile[0,0]
    
    FE = profile[:,1]
    dFE = np.zeros(len(pos))
    dFE[0] = (FE[1]-FE[0])/dpos
    dFE[-1] = (FE[-1]-FE[-2])/dpos

    
    for i in range(1,len(profile)-1):
        dFE[i] = (FE[i+1]-FE[i-1])/(2.*dpos)
    dFE_pos = []

    #for x in trajectory[1:-1,1]:
    for x in trajectory[unzoomedFactor:-unzoomedFactor:unzoomedFactor,1]:
        index_pos = math.floor((x-pos_min)/dpos)
        if index_pos < 0:
            index_pos = 0
        dFE_pos.append(dFE[index_pos])
        
    dFE_pos = np.array(dFE_pos)
    # print(dFE_pos)
    # exit()
        
    
   
    



G = (unzoomedAcc + gamma * unzoomedVel + dFE_pos/m) * np.sqrt(dt) *np.sqrt(6.)/2.0
unzoomedAcctest = - gamma * unzoomedVel - dFE_pos/m + G

plt.plot([t*newdt for t in range(len(unzoomedAcc))], unzoomedAcc, label='finite diff pos')
plt.plot([t*newdt for t in range(len(unzoomedAcctest))], unzoomedAcctest, label='corrected')
plt.plot([t*newdt for t in range(len(realAcc))], realAcc, label='real')
plt.legend()
plt.show()
sigma2 = 2.0*kT/m*gamma*dt
corrV2 = (2.0/3.0)*2.0*kT/m*gamma*dt 
print(corrV2)

a = kT/m
b = 2.0*(np.mean(unzoomedVel*dFE_pos/m) + kT/m)

c = np.mean(dFE_pos*dFE_pos)/(m*m) - np.mean(unzoomedAcctest*unzoomedAcctest)


g_p = (-b + np.sqrt(b*b-4.0*a*c))/(2.*a)
g_m = (-b - np.sqrt(b*b-4.0*a*c))/(2.*a)

print('<acc> = ' + str(np.mean(unzoomedAcc*unzoomedAcc)))
print('<acc> = ' + str(np.mean(realAcc*realAcc)))
print('gamma+ = ' + str(g_p))
print('gamma- = ' + str(g_m))
exit()


        


#