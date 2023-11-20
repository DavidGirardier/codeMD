import numpy as np
import math
from typing import List, TypeVar, Tuple, Dict, Set


def extractNoise(posp1, pos, posm1, time_resolution, prof):

    gamma = 1.
    mass = 1.
    force = 0.
    recovered_noise = (pos - posm1)/time_resolution - (1.0 -  gamma*time_resolution/2.0)*(posp1 - posm1)/time_resolution - 0.5*time_resolution*force/mass


kT=1


input_traj = '500TrajVECg_pos_2'
trajectories = np.loadtxt(input_traj)

input_prof = 'ProfGammaVECFractiondt0_001_2'
profile = np.loadtxt(input_prof)

pos = profile[:,0]
pos_min = profile[0,0]
dpos = profile[1,0]-profile[0,0]

FE = profile[:,1]
dFE = np.zeros(len(pos))
dFE[0] = (FE[1]-FE[0])/dpos
dFE[-1] = (FE[-1]-FE[-2])/dpos



gamma = profile[:,3]
dgamma = np.zeros(len(pos))
dgamma[0] = (gamma[1]-gamma[0])/dpos
dgamma[-1] = (gamma[-1]-gamma[-2])/dpos

mass = profile[0,4]

for i in range(1,len(profile)-1):
    dFE[i] = (FE[i+1]-FE[i-1])/(2.*dpos)
    dgamma[i] = (gamma[i+1]-gamma[i-1])/(2.*dpos)

t = trajectories[:,0]
x = trajectories[:,1]
v = trajectories[:,2]

dt = trajectories[1,0]-trajectories[0,0]


recovered_noise_list = []
for i in range(1,len(t)-1):
    

    if (t[i-1]<t[i]) and (t[i]<t[i+1]):
        index_pos = math.floor((x[i]-pos_min)/dpos)

        sigma = np.sqrt(2.*kT*gamma[index_pos]/mass)

        # recovered_noise = ((x[i+1] - x[i])/dt - 
        #                    (1.0 -  gamma[index_pos]*dt/2.0)*(x[i+1] - x[i-1])/dt 
        #                    - 0.5*dt*dFE[index_pos]/mass)*2.0/sigma
        print(v[i-1]-(x[i+1] - x[i-1])/dt)
        recovered_noise = ((x[i+1] - x[i])/dt - 
                           (1.0 -  gamma[index_pos]*dt/2.0)*v[i] 
                           - 0.5*dt*dFE[index_pos]/mass)*2.0/sigma
        recovered_noise_list.append(recovered_noise)


print(np.mean(recovered_noise_list))
print(np.var(recovered_noise_list))


import matplotlib.pyplot as plt
histo_noise = np.histogram(recovered_noise_list, np.arange(min(recovered_noise_list),max(recovered_noise_list),0.2))
plt.plot(histo_noise[1][:-1],histo_noise[0]/(len(recovered_noise_list)))
plt.show()



    
    

    
        
    