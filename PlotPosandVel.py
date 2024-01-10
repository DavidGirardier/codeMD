import numpy as np
import matplotlib.pyplot as plt

inputfile= 'lightOWHeavyC_1ns'

dt = 0.001

#dt=0.001

tFile = 5.
nLine = tFile/dt

trajectory = np.loadtxt(inputfile, max_rows=int(nLine)+1)
everyList = [1,10,20,50,100]
#plt.plot(trajectory[:,0], trajectory[:,1],label='position')
for every in everyList:

            positionAndvelocities = []
            
            for k in range(1+every,len(trajectory)-1*every,every):
                
                velocity = (trajectory[k+1*every][1]-trajectory[k-1*every][1])/(2.*dt*every)
                
                positionAndvelocities.append([trajectory[k][0], velocity])

            print((trajectory[3][1]-trajectory[1][1])/(2.*dt*every))
            print(positionAndvelocities[1][1])
            positionAndvelocities = np.array(positionAndvelocities)
            
            plt.plot(positionAndvelocities[:,0], positionAndvelocities[:,1],label='velocity every'+str(every))
plt.legend()
plt.show()
                
