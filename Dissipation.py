import numpy as np

from scipy.fftpack import fft, ifft, ifftshift

import matplotlib.pyplot as plt

def EnergyDoubleWell(x:float):
    barrier = 5.
    Energy = barrier*x**4 - 2.0*barrier*x**2
    #Force = -9.81
    # alpha = 0.
    # Force = -2.*x + 3.*alpha*x*x
    #Force=0.0
    #Force = -50*x
    return Energy

traj = np.loadtxt('500.0DW5_g2.0m1.0_1')

dt = 0.001
time = 2
ntraj = 200
m=1
gamma = 2
steps = int(time/dt+1)
Ecin = []
Epot = []

allFinalWork=[]

for i in range(ntraj):
    Work = 0
    Work_arr = [0]
    time_plot = []
    Ecin = []
    Epot = []
    v = []
    x = []
    for j in range(steps):
        
        #print(traj[i*steps+j,:])
        time_plot.append([traj[j,0]])
        Ecin.append(0.5*m*traj[i*steps+j,2]**2)
        v.append(traj[i*steps+j,2])
        x.append(traj[i*steps+j,1])
        Epot.append(EnergyDoubleWell(traj[i*steps+j,1]))
        
        if j!= 0 :
            dx = abs(traj[i*steps+j,1]- traj[i*steps+j-1,1])
            Work = Work + gamma * traj[i*steps+j,2] * dx 
            Work_arr.append(Work)
            if (traj[i*steps+j,1] > 1) or (traj[i*steps+j,1] < -1):
                FinalWork = Work
    #print('end')
    plt.plot(time_plot, x, label='traj')
    allFinalWork.append(abs(FinalWork))
    

    #plt.plot(time_plot, Ecin, label='Ecin')
    #plt.plot(time_plot, Epot, label='Epot')
    
    plt.plot(time_plot, Work_arr,'.', label='Work')
    # plt.legend()
    # plt.show()
    # exit()
# plt.plot(time_plot, Epot+Ecin, label='Etot')

plt.legend()
plt.show()
print("mean dissipativ work = " + str(np.mean(allFinalWork)))
exit()
    


