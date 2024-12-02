import numpy as np
from typing import List, TypeVar, Tuple, Dict, Set
from scipy.misc import derivative
import matplotlib.pyplot as plt
import math
import sys
from numba import jit
@jit(nopython=True)
def Milstein(profile, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory= []
    
    time= []
    
    #print(profile[:,0])
    mass = profile[1,4]
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
        
        
        time.append(i*timeStep)
        trajectory.append(x)
        #print(math.floor((x-pos_min)/dpos))

        index_pos = math.floor((x-pos_min)/dpos)
        
        if index_pos < 0:
            index_pos = 0
        
        sigma = np.sqrt(2.*kT*gamma[index_pos]/mass)

        randomNumber = np.random.normal()
        x_new = x + v*timeStep
        v_new = v - gamma[index_pos]*v*timeStep - timeStep*dFE[index_pos]/mass + np.sqrt(timeStep)*sigma*randomNumber + 0.5*dgamma[index_pos]/(kT*mass)*(randomNumber*randomNumber-1.)*timeStep

        
        x = x_new
        v = v_new
        #print(x)
        
        
        
    return time,trajectory
    sys.exit("exceeds runtime")
def gaussian(x,a):
    
    g = a*np.exp((-(x+1)**2)/0.05) + 1
    return g
    

def PotDW(x:float):
    barrier = 10.
    Pot = barrier*x**4 - 2.0*barrier*x**2

    return Pot


grid = np.linspace(-2,2,1000)

# FE=np.loadtxt("metaFE2")
# mass=(FE[:,0]**0)*7039.21
#gamma=(FE[:,0]**0)*0.59

# profile = np.column_stack((FE,FE[:,1]))
# profile = np.column_stack((profile,gamma))
# profile = np.column_stack((profile,mass))

pot = PotDW(grid)
gamma = gaussian(grid,2)
mass = grid**0
profile = grid
profile = np.column_stack((profile,pot))
profile = np.column_stack((profile,pot))
profile = np.column_stack((profile,gamma))
profile = np.column_stack((profile,mass))
np.savetxt("profile",np.c_[profile],fmt='%1.8E')
pot = PotDW(grid)
gamma = gaussian(grid,0)
mass = grid**0
profile2 = grid
profile2 = np.column_stack((profile2,pot))
profile2 = np.column_stack((profile2,pot))
profile2 = np.column_stack((profile2,gamma))
profile2 = np.column_stack((profile2,mass))

np.savetxt("profile2",np.c_[profile2],fmt='%1.8E')

kT = 1.
x0 = 0.

dt=0.001
t=5.
PrintTraj = True
lenght = int(t/dt) + 1

numberOfTraj = 10000.

for j in range(int(numberOfTraj)):

    print(j)
    v0 = np.sqrt(kT/mass[0]) * np.random.normal()
    time, traj = Milstein(profile, kT, x0, v0, dt, t)
    np.savetxt("traj_gauss"+str(j), np.c_[time,traj], fmt='%1.8E')
    time, traj = Milstein(profile2, kT, x0, v0, dt, t)
    np.savetxt("traj_nogauss"+str(j), np.c_[time,traj], fmt='%1.8E')