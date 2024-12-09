import scipy.integrate as integrate
import numpy as np
input_name = 'V2normntraj10000_Z2g5.0m1.0_ratio_0.5'
trajectories = np.loadtxt(input_name)

integrale = integrate.cumtrapz(trajectories[1:,1],trajectories[1:,0])    
outputName= 'Integral_'+input_name

np.savetxt(outputName, np.c_[trajectories[1:-1,0],integrale], fmt='%1.8E')