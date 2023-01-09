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

def cubicSpline(a, b, c, d, x, numberOfSplines, Interval):
    y = zeros(len(x))
    sizeSpline = Interval/numberOfSplines
    border = arange(minPos,maxPos,sizeSpline)
    print(border)

    for h in range(len(x)):
        for i in range(len(border)-1):
            if (x[h] >= border[i]) and  (x[h] < border[i+1]):
                print(a[i],b[i],c[i],d[i])
                
                y[h] = a[i]*(x[h] - i*sizeSpline)**3 + b[i]*(x[h] - i*sizeSpline)**2 + c[i]*(x[h] - i*sizeSpline) + d[i]
                #print(xlocal)
    return y

minPos = 1.
maxPos = 10.
x = arange(minPos,maxPos,0.01)
Interval = abs(x[-1] - x[0])
a = [0,-1,1]
b = [2,0,0]
c = [0,0,0]
d = [1.0,2.0,5.0]
y = cubicSpline(a, b, c, d, x, 3, Interval)

plt.plot(x,y)
plt.show()

# pointsToInterpolate = np.zeros(len(x))

# start = 100
# aguess = np.zeros(20)
# profile = loadtxt('profile.txt')
# x = profile[start:-start,0]
# #pointsToInterpolate = 1./profile[:,3]
# pointsToInterpolate = profile[start:-start,1]
#res = minimize(differencewithPowerSeries, aguess, args=(x, pointsToInterpolate), method='CG', options={'xatol': 1e-8, 'disp': True})
# x = profile[:,0]
# y = profile[:,1]
# print(x)
# f = interp1d(x, y, kind='cubic')
# barrier = 5
# pointsToInterpolate = zeros(len(x))
# for j in range(0, len(x)):
#     pointsToInterpolate[j] = barrier*x[j]**4 - 2.0*barrier*x[j]**2 + barrier#+ 0.5*x[j] + 1 + 0.01*np.random.rand()

# print(res.x)
# plt.plot(profile[:,0],(profile[:,1]), "o")
# #plt.plot(x,pointsToInterpolate)
# #plt.plot(x,powerSeries(res.x,x))
# plt.plot(x,f(x))
# plt.show()
# print(x)
# savetxt('iniPROFILE', c_[x, pointsToInterpolate, pointsToInterpolate, 0.1*profile[:,3], profile[:,4]], header='x F F/kT gamma mass')

