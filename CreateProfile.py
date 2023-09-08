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

#x = arange(-1.5,1.5,0.01)
#pointsToInterpolate = zeros(len(x))

# start = 100
# aguess = np.zeros(20)
profile = loadtxt('profile.txt')
#x = profile[start:-start,0]
# #pointsToInterpolate = 1./profile[:,3]
# pointsToInterpolate = profile[start:-start,1]
#res = minimize(differencewithPowerSeries, aguess, args=(x, pointsToInterpolate), method='CG', options={'xatol': 1e-8, 'disp': True})
x = profile[:,0]


# ngrid = 1000
# start = 0.954697
# end = 1.881799
# x = arange(start,end+(end-start)/1000.,(end-start)/1000.)

#x = arange(-1.5,1.5,0.01)
# y = profile[:,1]
# print(x)
# f = interp1d(x, y, kind='cubic')
barrier = 10.
pointsToInterpolate = zeros(len(x))
mass = zeros(len(x))
for j in range(0, len(x)):
    pointsToInterpolate[j] = barrier*x[j]**4 - 2.0*barrier*x[j]**2 + barrier#+ 0.5*x[j] + 1 + 0.01*np.random.rand()
    mass[j] = x[j]**2 + 1.0

# print(res.x)
# plt.plot(profile[:,0],(profile[:,1]), "o")
# #plt.plot(x,pointsToInterpolate)
# #plt.plot(x,powerSeries(res.x,x))
# plt.plot(x,f(x))
# plt.show()
print(x)
#savetxt('iniPROFILE', c_[x, 0.*x**0, 0.*x**0, 10.*x**0, 1.*x**0], header='x F F/kT gamma mass')
#savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 5.*profile[:,3]**0, 1.*mass**0], header='x F F/kT gamma mass')
#savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 5.33*profile[:,3]**0, 1.*mass**0], header='x F F/kT gamma mass') #no Umbrella
#savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 4.88*profile[:,3]**0, 1.03*mass**0], header='x F F/kT gamma mass') #ev 10
#savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 4.33*profile[:,3]**0, 1.25*mass**0], header='x F F/kT gamma mass') #ev 25
#savetxt('iniPROFILE', c_[x, 0.*pointsToInterpolate, 0.*pointsToInterpolate, 5.*profile[:,3]**0, 1.*mass**0], header='x F F/kT gamma mass')


#savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 5.33*profile[:,3]**0, 1.*mass**0], header='x F F/kT gamma mass') #no Umbrella
#savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 5.12*profile[:,3]**0, 1.03*mass**0], header='x F F/kT gamma mass') #ev 10
savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 4.53*profile[:,3]**0, 1.25*mass**0], header='x F F/kT gamma mass') #ev 25



