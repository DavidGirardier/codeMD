import scipy.integrate as integrate
import numpy as np
input_name = 'memory_true.dat'
trajectories = np.loadtxt(input_name)
#print(trajectories[:,0])
#int_list = []
# for i in range(2,len(trajectories[1:,0])):
#     #print(trajectories[1:i,1])
#     #print(trajectories[1:i,0])
#     integrale = integrate.cumtrapz(trajectories[1:i+1,1],trajectories[1:i+1,0])
#     print(integrale)
#     int_list.append(integrale)
integrale = integrate.cumtrapz(trajectories[1:,1],trajectories[1:,0])    
outputName= 'Integral_'+input_name

np.savetxt(outputName, np.c_[trajectories[1:-1,0],integrale], fmt='%1.8E')