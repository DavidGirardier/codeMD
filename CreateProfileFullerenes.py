from tokenize import Pointfloat
from numpy import transpose, sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz, transpose, zeros

import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.interpolate import interp1d
def powerSeries(a, x):
    i = 0
    y = zeros(len(x))
    print(y)
    for i in range(0, len(a)):
        for j in range(0, len(x)):
            y[j] += a[i]*x[j]**i
    return y

def differencewithPowerSeries(a, x, pointsToInterpolate):
    y = powerSeries(a, x)
    difference = 0
    for j in range(0, len(x)):
        difference =  difference + abs(pointsToInterpolate[j] - y[j])
    return difference




# ngrid = 1000
# start = 0.956217038
# end = 1.8493922
# x = arange(start,end+(end-start)/1000.,(end-start)/1000.)


##### In the well ######
# ngrid = 1000
# end = 1.190208
# start = 0.9505
# x = arange(start,end+(end-start)/1000.,(end-start)/1000.)

ngrid = 1000
start = 0.945226316 #500Colvar
end = 1.80057894

# ngrid = 1000 #10ns well Nobaro
# start=0.94
# end=1.32

# start = 0.955868257 #1000 nonreact+react
# end = 1.93039072

# end = 1.65346339 #t =10
# start = 0.95855738

# end = 2.9591493419859285 #20x5ns
# start = 0.9402985709792403

# end = 2.42650287 #20*80ps
# start = 0.940298571

# start = 0.945999206 #40*120ps
# end = 2.68261661

# start = 0.945999206 #40*220ps
# end = 2.93260229

x = arange(start,end+(end-start)/1000.,(end-start)/1000.)



print(x)
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 2.18*x**0, 666.30*x**0], header='x F F/kT gamma mass') #ev400
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 2.23*x**0, 395.63*x**0], header='x F F/kT gamma mass') #ev300
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 2.38*x**0, 245.54*x**0], header='x F F/kT gamma mass') #ev200
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 2.73*x**0, 172.08*x**0], header='x F F/kT gamma mass') #ev100
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 2.91*x**0, 147.67*x**0], header='x F F/kT gamma mass') #ev1
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 7.11*x**0, 147.67*x**0], header='x F F/kT gamma mass') #ev1 kernel
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 3.83*x**0, 147.67*x**0], header='x F F/kT gamma mass') #ev1 k*1.17 (US)
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 2.80*x**0, 147.67*x**0], header='x F F/kT gamma mass') #ev1 k linear fit
#savetxt('iniPROFILEFULL', c_[x, pointsToInterpolate, pointsToInterpolate, 0.01*profile[:,3], mass], header='x F F/kT gamma mass')
#savetxt('iniPROFILEFULL', c_[x, 0.*pointsToInterpolate, 0.*pointsToInterpolate, 1.*profile[:,3]**0, mass], header='x F F/kT gamma mass')
#savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 0.1*x**0, 172.08*x**0], header='x F F/kT gamma mass') #ev100
savetxt('iniPROFILEFULL', c_[x, 0.*x, 0.*x, 0.1*x**0, 147.67*x**0], header='x F F/kT gamma mass') #ev1 k linear fit
