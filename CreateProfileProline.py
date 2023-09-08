from tokenize import Pointfloat
from numpy import transpose, sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz, transpose, zeros

import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.interpolate import interp1d



ngrid = 1000
start = -0.7 #500Colvar
end = 3.85

#3.806422307179586, -0.660545

x = arange(start,end+(end-start)/1000.,(end-start)/1000.)



print(x)
#savetxt('iniPROFILEpro', c_[x, 0.*x, 0.*x, 10.*x**0, 0.05741873*x**0], header='x F F/kT gamma mass') #ev1 kernel
savetxt('iniPROFILEpro', c_[x, 0.*x, 0.*x, 40.*x**0, 0.12*x**0], header='x F F/kT gamma mass') #ev1 kernel
