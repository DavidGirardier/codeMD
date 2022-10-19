from tokenize import Pointfloat
from numpy import sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz, transpose, zeros

import matplotlib.pyplot as plt
from scipy.optimize import minimize
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
pointsToInterpolate = zeros(len(x))
for j in range(0, len(x)):
    pointsToInterpolate[j] = 5.*x[j]**4 - 10.*x[j]**2 + 5.#+ 0.5*x[j] + 1 + 0.01*np.random.rand()

# print(res.x)
#plt.plot(profile[:,0],(1./profile[:,3]))
plt.plot(x,pointsToInterpolate)
#plt.plot(x,powerSeries(res.x,x))
plt.show()
savetxt('PROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, profile[:,3], profile[:,4]])

