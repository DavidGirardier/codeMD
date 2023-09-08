import numpy as np
from typing import List, TypeVar, Tuple, Dict, Set
from scipy.misc import derivative
import matplotlib.pyplot as plt
import math
import sys

def Milstein(profile, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []
    g:List[float] = []
    #print(profile[:,0])
    pos = profile[:,0]
    pos_min = profile[0,0]
    dpos = profile[1,0]-profile[0,0]
    
    FE = profile[:,1]
    dFE = np.zeros(len(pos))
    dFE[0] = (FE[1]-FE[0])/dpos
    dFE[-1] = (FE[-1]-FE[-2])/dpos

    # test = [i*i for i in pos]
    # dtest = np.zeros(len(pos))

    gamma = profile[:,3]
    dgamma = np.zeros(len(pos))
    dgamma[0] = (gamma[1]-gamma[0])/dpos
    dgamma[-1] = (gamma[-1]-gamma[-2])/dpos
    
    for i in range(1,len(profile)-1):
        dFE[i] = (FE[i+1]-FE[i-1])/(2.*dpos)
        dgamma[i] = (gamma[i+1]-gamma[i-1])/(2.*dpos)
        # dtest[i] = (test[i+1]-test[i-1])/(2.*dpos)
    #plt.plot(pos, test)   
    # plt.plot(pos, dtest)
    # plt.show()

    # exit()
    v = initialVelocity 
    x = initialPosition
    
    for i in range(int(totalTime/timeStep)+1):
        # trajectory.append(x)
        # velocities.append(v)
        #time.append(i*timeStep)
        
        #print(x)
        
        index_pos = math.floor((x-pos_min)/dpos)
        if index_pos < 0:
            index_pos = 0
       
        sigma = np.sqrt(2.*kT*gamma[index_pos]/mass)

        randomNumber = np.random.normal()
        x_new = x + v*timeStep
        v_new = v - gamma[index_pos]*v*timeStep - timeStep*dFE[index_pos]/mass + np.sqrt(timeStep)*sigma*randomNumber + 0.5*dgamma[index_pos]/(kT*mass)*(randomNumber*randomNumber-1.)*timeStep

        g.append(randomNumber)
        x = x_new
        v = v_new
        if x > 1.325 :
            
            return i*timeStep
    return i*timeStep
    sys.exit("exceeds runtime")

def CicottiVandenEijdenFP(profile, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, maximumPosition:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []



    pos = profile[:,0]
    pos_min = profile[0,0]
    dpos = profile[1,0]-profile[0,0]
    
    FE = profile[:,1]
    dFE = np.zeros(len(pos))
    dFE[0] = (FE[1]-FE[0])/dpos
    dFE[-1] = (FE[-1]-FE[-2])/dpos

    # test = [i*i for i in pos]
    # dtest = np.zeros(len(pos))

    gamma = profile[:,3]
    dgamma = np.zeros(len(pos))
    dgamma[0] = (gamma[1]-gamma[0])/dpos
    dgamma[-1] = (gamma[-1]-gamma[-2])/dpos
    
    for i in range(1,len(profile)-1):
        dFE[i] = (FE[i+1]-FE[i-1])/(2.*dpos)
        dgamma[i] = (gamma[i+1]-gamma[i-1])/(2.*dpos)


    v = initialVelocity 
    x = initialPosition
    
    for i in range(int(totalTime/timeStep)+1):
        # trajectory.append(x)
        # velocities.append(v)
        # time.append(i*timeStep)
        
        randomNumber1 = np.random.normal()
        randomNumber2 = np.random.normal()

        index_pos = math.floor((x-pos_min)/dpos)
        if index_pos < 0:
            index_pos = 0

        sigma = np.sqrt(2.*kT*gamma[index_pos]/mass)

        #A=0.0
        A = 0.5*(timeStep**2.)*(-dFE[index_pos]/mass-gamma[index_pos]*v) + sigma*(timeStep**(3./2.))*(0.5*randomNumber1 + 1./(2.*np.sqrt(3))*randomNumber2)
        x_new = x + timeStep*v + A
        #print(x_new)
        nindex_pos = math.floor((x_new-pos_min)/dpos)
        if nindex_pos < 0:
            nindex_pos = 0

        v_new = v - timeStep*gamma[nindex_pos]*v - 0.5*timeStep*(dFE[nindex_pos]+dFE[index_pos])/mass + np.sqrt(timeStep)*sigma*randomNumber1 - gamma[index_pos]*A

        
        x = x_new
        v = v_new
        if x > maximumPosition :
            return i*timeStep
        
    return i*timeStep

beg_input = "ProfFixedGM4_53and1_25_fraction500TrajVECDW10m1g5t2psdt0_001_newdt0_05"
MFPT=[]
numberOfSample = 5
for k in range(1,numberOfSample+1):
    inputfile = beg_input + '_' + str(int(k))
    profile = np.loadtxt(inputfile)


    kT=1.
    mass = profile[1,4]
    print(mass)
    x0 = -1.0
    xmax = 1.0
    v0 = np.sqrt(kT/mass) * np.random.normal()
    dt = 0.001
    maxTime = 100000.
    timeEscape = []
    
    
    for i in range(100):
        print(i)
        #time = Milstein(profile, kT, x0, v0, dt, maxTime)
        time = CicottiVandenEijdenFP(profile, kT, x0, v0, dt, xmax, maxTime)
        timeEscape.append(time)

    print(np.mean(timeEscape))
    MFPT.append(np.mean(timeEscape))
    print(inputfile)

print(beg_input)
print('mean MFPT : ' + str(np.mean(MFPT)))
print('std dev MFPT : ' + str(np.sqrt(np.var(MFPT)/numberOfSample)))



# outputName='TrajReconstructed'
# np.savetxt(outputName, np.c_[time,traj], fmt='%1.8E')