import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pot import Z1, Z2
import glob

def hbq(x, r):
    if x > r :
        return 1
    else:
        return 0

def theta(x):
    if x > 0:
        return 1
    else:
        return 0


inputfile= 'ntraj10000_Z1g5.0m1.0'

ratio_list = np.linspace(0,1,11)

for ratio in ratio_list:
    print(str(ratio))


    r=0

    files= glob.glob(inputfile+'*')

    dt=0.001
    traj1 = np.loadtxt(files[0])
    trans_n = np.zeros((len(files),len(traj1[:,1])))
    trans_d = np.zeros((len(files)))

    for j in range(len(files)):
        print(j)
        TwoDtrajectory = np.loadtxt(files[j])
        time=TwoDtrajectory[:,0]
        x=TwoDtrajectory[:,1]
        y=TwoDtrajectory[:,2]
        combination = -1.0*(ratio * x + (1.0-ratio)*y)
        trajectory=combination
        ini_vel = (trajectory[1]-trajectory[0])/dt
        #print(ini_vel)
        for t in range(len(trajectory)):
            trans_n[j,t] = ini_vel*hbq(trajectory[t],r)
        
        trans_d[j] = ini_vel*theta(ini_vel)
        
        

    transmission = np.mean(trans_n,axis=0)/np.mean(trans_d)
    # plt.plot(traj1[:,0],transmission)
    # plt.show()

    np.savetxt("tc_ratio_" + str(ratio)[0:3]+inputfile, np.c_[traj1[:,0],transmission])