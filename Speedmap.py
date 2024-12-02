import numpy as np
import math
from typing import List, TypeVar, Tuple, Dict, Set

from scipy.fftpack import fft, ifft, ifftshift

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def speed_map(traj):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    n_bin=11.
    vbyq=np.zeros((len(traj),2))
    print(vbyq)
    dt = traj[1,0] - traj[0,0]
    
    for i in range(1,len(traj)-1):
        if traj[i,0] < traj[i+1,0]:
            
            vel = (traj[i+1,1]-traj[i-1,1])/(2.*dt)
            vbyq[i,0]=traj[i,1]
            vbyq[i,1]=vel
    
    space = np.max(traj[:,1])-np.min(traj[:,1])
    print(space)
    bin_size=space/n_bin

    for i in range(int(n_bin)):
        print(str(i)+'/11')
        bin_sample=[]
        for j in range(len(vbyq)):
            if (vbyq[j,0]>(np.min(traj[:,1])+i*bin_size)) & (vbyq[j,0]<(np.min(traj[:,1])+(i+1)*bin_size)):
                bin_sample.append(vbyq[j,1])

        #hist_bybin = np.histogram(bin_sample, np.linspace(np.min(vbyq),np.max(vbyq),60))
        hist_bybin = np.histogram(bin_sample, np.linspace(-1.5,1.5,20))
        # mean_ts = np.mean(noise_bin_ts[:,1])

        # var_ts = np.var(noise_bin_ts[:,1])
        #plt.plot(histo_noise_all[1][:-1],histo_noise_all[0]/len(noise)*10,label='All, mean=' + str(mean_all) + ', var='+str(var_all))
        ax.scatter((np.min(traj[:,1])+i*bin_size)*np.ones(len(hist_bybin[1][:-1])), hist_bybin[1][:-1], hist_bybin[0]/len(bin_sample))
        posBin = np.min(traj[:,1]) + bin_size*i
        posBin = float("{:.2f}".format(posBin))
        np.savetxt('q'+str(posBin) + '_hist', np.c_[hist_bybin[1][:-1],hist_bybin[0]/len(bin_sample)], fmt='%1.8E')

        #plt.plot(hist_bybin[1][:-1], hist_bybin[0]/len(bin_sample))
    #Set labels and title
    # ax.scatter((np.min(traj[:,1])+np.ones(int(n_bin))*bin_size), np.zeros(int(n_bin)),np.zeros(int(n_bin)))
    
    # ax.set_xlabel('q')
    # ax.set_ylabel('v')
    # ax.set_zlabel('P(v|q)')
    # ax.set_title('Velocity Distribution in 3D')
    # plt.show()                  


    return

traj_file = 'testSpeed'
#traj_file = 'fraction500TrajMilsteing_posm1_newdt0_005_1'
traj = np.loadtxt(traj_file)   

speed_map(traj)



