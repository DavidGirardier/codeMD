import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython=True)
def EulerMaruyamaOLE(mass, diffusion, kT, initialPosition, timeStep, totalTime,Pot):
    trajectoryx= []
    trajectoryy= []
    alldx=[]
    alldy=[]

    time= []
    
    x = initialPosition[0]
    y = initialPosition[1]


    
    for i in range(int(totalTime/timeStep)+1):
        trajectoryx.append(x)
        trajectoryy.append(y)
        

        
        time.append(i*timeStep)
        
        Fx, Fy, _ = Pot(x,y)
        Fx = -Fx
        Fy = -Fy

        randomNumberx = np.random.normal()
        randomNumbery = np.random.normal()

    
   
        Dx = diffusion[0]
        Dy = diffusion[1]


        


        dx = timeStep*Fx*Dx + np.sqrt(2.*Dx*timeStep)*randomNumberx
        dy = timeStep*Fy*Dy + np.sqrt(2.*Dy*timeStep)*randomNumbery
        x_new = x + timeStep*Fx*Dx + np.sqrt(2.*Dx*timeStep)*randomNumberx
        y_new = y + timeStep*Fy*Dy + np.sqrt(2.*Dy*timeStep)*randomNumbery

       
        alldx.append(dx)
        alldy.append(dy)
        
        
        x = x_new
        y = y_new

    return time, trajectoryx, trajectoryy, alldx, alldy#, velocitiesx, velocitiesy