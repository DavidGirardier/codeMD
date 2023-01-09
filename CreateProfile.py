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

# x = np.arange(-1.5,1.5,0.01)
# pointsToInterpolate = np.zeros(len(x))

# start = 100
# aguess = np.zeros(20)
profile = loadtxt('profile.txt')
# x = profile[start:-start,0]
# #pointsToInterpolate = 1./profile[:,3]
# pointsToInterpolate = profile[start:-start,1]
#res = minimize(differencewithPowerSeries, aguess, args=(x, pointsToInterpolate), method='CG', options={'xatol': 1e-8, 'disp': True})
x = profile[:,0]
y = profile[:,1]
print(x)
f = interp1d(x, y, kind='cubic')
barrier = 5
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
savetxt('iniPROFILE', c_[x, 0.*pointsToInterpolate, 0.*pointsToInterpolate, 10*profile[:,3]**0, 1*mass**0], header='x F F/kT gamma mass')
#savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 10*profile[:,3]**0, mass**0], header='x F F/kT gamma mass')

