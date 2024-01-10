import numpy as np
import math
from typing import List, TypeVar, Tuple, Dict, Set

from scipy.fftpack import fft, ifft, ifftshift

import matplotlib.pyplot as plt

def autocorrelationFFT(x):
    xp = ifftshift((x - np.average(x))/np.std(x))
    n, = xp.shape
    xp = np.r_[xp[:n//2], np.zeros_like(xp), xp[n//2:]]
    f = fft(xp)
    p = np.absolute(f)**2
    pi = ifft(p)
    return np.real(pi)[:n//2]/(np.arange(n//2)[::-1]+n//2)


recovered_noise_matrix = []
histo_noise_matrix = []
noise_corr_matrix = []

kT=1.0
numberOfSample = 5
for sample in range(1,numberOfSample+1):
    
    #input_traj = 'fraction500TrajMilsteing_gammasmallposm1_newdt0_005_2'
    input_traj = 'fraction500traj2ps_newdt0_02'
    trajectories = np.loadtxt(input_traj+'_'+str(sample))

    #input_prof = 'ProfLessOpti5Loop_fraction500TrajMilsteing_gammasmallposm1_newdt0_005_2'
    input_prof = 'Proffraction500traj2ps_newdt0_02'
    #input_prof = 'ProfGammaVECFractiondt0_001_5Loop_1'
    #input_prof = 'Proffraction500TrajMilsteing_gammasmallposm1_newdt0_005_1Loop_1'
    profile = np.loadtxt(input_prof+'_'+str(sample)+'Loop_5')

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
    #v = trajectories[:,2]

    dt = trajectories[1,0]-trajectories[0,0]


    recovered_noise_list = []
    for i in range(1,len(t)-1):
        

        if (t[i-1]<t[i]) and (t[i]<t[i+1]):
            index_pos = math.floor((x[i]-pos_min)/dpos)

            sigma = np.sqrt(2.*dt*kT*gamma[index_pos]/mass)

            recovered_noise = ((x[i+1] - x[i])/dt - 
                            (1.0 -  gamma[index_pos]*dt/2.0)*(x[i+1] - x[i-1])/(2.*dt)
                            + 0.5*dt*dFE[index_pos]/mass)*2.0/sigma

            # recovered_noise = ((x[i+1] - x[i])/dt - 
            #                    (1.0 -  gamma[index_pos]*dt/2.0)*v[i] 
            #                    + 0.5*dt*dFE[index_pos]/mass)*2.0/sigma
            recovered_noise_list.append(recovered_noise)


    print(np.mean(recovered_noise_list))
    print(np.var(recovered_noise_list))

    recovered_noise_matrix.append(recovered_noise_list)

    #print(recovered_noise_matrix)

    noise_corr = autocorrelationFFT(recovered_noise_list)
    noise_corr_matrix.append(noise_corr)

    #print(noise_corr)



    # histo_noise = np.histogram(recovered_noise_list, np.arange(min(recovered_noise_list),max(recovered_noise_list),0.2))
    histo_noise = np.histogram(recovered_noise_list, np.linspace(-3,3,30),0.2)
    histo_noise_matrix.append(histo_noise[0]/(len(recovered_noise_list)))


mean_histo_noise = np.mean(histo_noise_matrix,axis=0)
std_histo_noise = np.std(histo_noise_matrix,axis=0)
plt.plot(histo_noise[1][:-1],mean_histo_noise)
plt.show()

mean_noise_corr = np.mean(noise_corr_matrix,axis=0)
std_noise_corr = np.std(noise_corr_matrix,axis=0)
plt.plot(np.arange(10),mean_noise_corr[0:10])
plt.show()

outputName = 'MeanAndErrorHisto'+'_'+input_prof
np.savetxt(outputName, np.c_[histo_noise[1][:-1],mean_histo_noise,std_histo_noise/np.sqrt(numberOfSample)], fmt='%1.8E')
outputName = 'MeanAndErrorCorr'+'_'+input_prof
np.savetxt(outputName, np.c_[np.arange(len(mean_noise_corr)),mean_noise_corr, std_noise_corr/np.sqrt(numberOfSample)], fmt='%1.8E')

#print(np.var(recovered_noise_matrix,axis=1))
print('Mean = ', np.mean(np.mean(recovered_noise_matrix,axis=1)))
print('Var = ',np.mean(np.var(recovered_noise_matrix,axis=1)))
print('Err on var = ', np.std(np.var(recovered_noise_matrix,axis=1))/np.sqrt(numberOfSample))


print('<G(t)G(t+1)> = ', mean_noise_corr[1])  
arr = np.array(noise_corr_matrix)
  
print('Err on corr = ',np.std(arr[:,1])/np.sqrt(numberOfSample)) 


    
        
    