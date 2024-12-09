import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython=True)
def EulerMaruyama(mass, gamma, kT, initialPosition, initialVelocity, timeStep, totalTime,Pot):
    trajectoryx= []
    trajectoryy= []

    velocitiesx= []
    velocitiesy= []
    time= []
    
    x = initialPosition[0]
    y = initialPosition[1]

    vx = initialVelocity[0]
    vy = initialVelocity[1]
    
    for i in range(int(totalTime/timeStep)+1):
        trajectoryx.append(x)
        trajectoryy.append(y)
        
        velocitiesx.append(vx)
        velocitiesy.append(vy)
        
        time.append(i*timeStep)
        
        Fx, Fy, _ = Pot(x,y)
        Fx = -Fx
        Fy = -Fy

        randomNumberx = np.random.normal()
        randomNumbery = np.random.normal()
        
        x_new = x + vx*timeStep
        sigma = np.sqrt(2.*kT*gamma/mass)
        vx_new = vx - gamma*vx*timeStep + timeStep*Fx/mass + np.sqrt(timeStep)*sigma*randomNumberx 
              
        y_new = y + vy*timeStep
        sigma = np.sqrt(2.*kT*gamma/mass)
        vy_new = vy - gamma*vy*timeStep + timeStep*Fy/mass + np.sqrt(timeStep)*sigma*randomNumbery
        
        x = x_new
        y = y_new
        vx = vx_new
        vy = vy_new
    return time, trajectoryx, trajectoryy#, velocitiesx, velocitiesy