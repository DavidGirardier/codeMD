import numpy as np
import math
from typing import List, TypeVar, Tuple, Dict, Set

from scipy.fftpack import fft, ifft, ifftshift

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def speed_map(traj):

    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    n_bin=11.
    vbyq=np.zeros((len(traj),2))

    dt = traj[1,0] - traj[0,0]
    q_array = []
    m_array = []

    for i in range(1,len(traj)-1):
        #if traj[i,0] < traj[i+1,0]:
        if (abs(abs(traj[i,0] - traj[i+1,0]) - dt) < dt/100.):
            
            vel = (traj[i+1,1]-traj[i-1,1])/(2.*dt)
            vbyq[i,0]=traj[i,1]
            vbyq[i,1]=vel
        # else :
        #     print(traj[i,0])
        #     print(i)
    
    space = np.max(traj[:,1])-np.min(traj[:,1])
    print(space)
    bin_size=space/n_bin

    for i in range(int(n_bin)):
        print(str(i)+'/'+str(int(n_bin)))
        vel_sample=[]
        for j in range(len(vbyq)):
            if (vbyq[j,0]>(np.min(traj[:,1])+i*bin_size)) & (vbyq[j,0]<(np.min(traj[:,1])+(i+1)*bin_size)):
                vel_sample.append(vbyq[j,1]*vbyq[j,1])
                #print(i)
        #print(vel_sample)
        
        mass_sample = 1./(np.mean(vel_sample))
        
        q_value = i*bin_size + np.min(traj[:,1])
        print(q_value)
        m_array.append(mass_sample)
        q_array.append(q_value)

        plt.plot(q_value, mass_sample, '.')
        # hist_bybin = np.histogram(bin_sample, np.linspace(-1.5,1.5,20))
        
        # ax.scatter((np.min(traj[:,1])+i*bin_size)*np.ones(len(hist_bybin[1][:-1])), hist_bybin[1][:-1], hist_bybin[0]/len(bin_sample))
        # posBin = np.min(traj[:,1]) + bin_size*i
        # posBin = float("{:.2f}".format(posBin))
        # np.savetxt('q'+str(posBin) + '_hist', np.c_[hist_bybin[1][:-1],hist_bybin[0]/len(bin_sample)], fmt='%1.8E')
        
    mass =  np.c_[q_array,m_array]   
    #plt.show()
    return mass

#traj_file = 'filtered_comm_ntraj10_Z1g5.0m1.0_6'
traj_file=str(input('name file:'))
#traj_file = 'fraction500TrajMilsteing_posm1_newdt0_005_1'
dt=0.001
traj = np.loadtxt(traj_file)   

m = speed_map(traj)

outputName = 'mass_' + traj_file 
np.savetxt(outputName, m, fmt='%1.4E') 


