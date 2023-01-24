from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt

dx = 0.1
noise = np.loadtxt('colvar_disp_scaled_from_prop')
#noise = np.loadtxt('fort.654')
histo_noise = np.histogram(noise[:,1], np.arange(-3.0,3.0,dx)) 

np.savetxt('Histo_ReproducedNoise', np.c_[histo_noise[1][:-1],histo_noise[0]/(len(noise[:,1]))], fmt='%1.8E')
noise2 = [x*x for x in noise[:,1]]
print('<noise> = ' + str(np.mean(noise)))
print('<noise^2> - <noise>^2 = ' + str(np.mean(noise2) - np.mean(noise)*np.mean(noise)))
print('integral = ' + str(np.trapz(histo_noise[0]/(len(noise[:,1])*dx), dx=0.1)))