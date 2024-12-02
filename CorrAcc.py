import numpy as np

from scipy.fftpack import fft, ifft, ifftshift

import matplotlib.pyplot as plt

def autocorrelation(data):
    
    x = np.array(data) 

    # Mean
    mean = np.mean(data)

    # Variance
    var = np.var(data)

    # Normalized data
    ndata = data #- mean

    acorr = np.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
    #acorr = acorr / var / len(ndata)

    return acorr


def correlation(datax,datay):
    
    x = np.array(datax) 

    # Mean
    meanx = np.mean(datax)

    # Variance
    varx = np.var(datax)

    # Normalized data
    ndatax = datax - meanx

    y = np.array(datay) 

    # Mean
    meany = np.mean(datay)

    # Variance
    vary = np.var(datay)

    # Normalized data
    ndatay = datay - meany

    meanxy = np.mean(x*y) - np.mean(x)*np.mean(x)

    acorr = np.correlate(ndatax, ndatay, 'full')[len(ndatax)-1:] 
    #corr = acorr / meanxy / len(ndatax)
    
    return acorr

def mycorrelation(datax,datay):
    sum = 0.
    for t in range(len(datax)):
        sum = datax[0]*datay[t]

    
    return 



def dFdq(x:float):
    barrier = 10.
    Force = 4.0*barrier*x**3 - 4.0*barrier*x
    #Force = -9.81
    # alpha = 0.
    # Force = -2.*x + 3.*alpha*x*x
    Force=0.0

    return Force

# inputfile = input('Trajectory File:')
# trajectories = np.loadtxt(inputfile, max_rows=2)
inputfile= 'EulerFP0.5m1.0_1'
unzoomedFactor = 1

trajectory = np.loadtxt(inputfile, skiprows=0, max_rows=10)
dt = trajectory[1,0]-trajectory[0,0]
print(dt)
mass = 1
#dt=0.001
numberOfTraj = 1
tFile = 500
nLine = tFile/dt
newdt = dt * unzoomedFactor

matrixXAC = []
matrixVAC = []

for i in range(numberOfTraj):
    trajectory = np.loadtxt(inputfile, skiprows=int(nLine)*i, max_rows=int(nLine)+1)

    unzoomedPos = [x for x in trajectory]
    unzoomedVel = [(trajectory[i+1*unzoomedFactor,1]-trajectory[i-1*unzoomedFactor,1])/(2.*dt*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    unzoomedAcc = [(trajectory[i+1*unzoomedFactor,1]-2.*trajectory[i,1]+trajectory[i-1*unzoomedFactor,1])/(dt*dt*unzoomedFactor*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    #unzoomedVel = [(trajectory[1,1]-trajectory[0,1])/dt] + unzoomedVel + [(trajectory[-1,1]-trajectory[-2,1])/dt] 
    # matrixXAC.append(autocorrelation(trajectory[::unzoomedFactor,1]))
    # matrixVAC.append(autocorrelation(unzoomedVel))

    # matrixXAC.append(autocorrelationFFT(trajectory[::unzoomedFactor,1]))
    # matrixVAC.append(autocorrelationFFT(unzoomedVel))

    # matrixXAC.append(signal.correlate(trajectory[::unzoomedFactor,1],trajectory[::unzoomedFactor,1]))
    # matrixVAC.append(signal.correlate(unzoomedVel,unzoomedVel))
    # corrVel = autocorrelation(unzoomedVel)
    # corrVel2 = correlation(unzoomedVel,unzoomedVel)
    #corrAcc = autocorrelation(unzoomedAcc)
    realAcc = [a for a in trajectory[:,3]]
    #realAcc = np.zeros(len(unzoomedVel))
    #realVel = [v for v in trajectory[1:-1,2]]
    realVel = [v for v in trajectory[1:-1,2]]
    dFdq_t= [dFdq(x) for x in trajectory[1:-1,1]] 

    force_q = [-dFdq(x)/mass for x in trajectory[1:-1,1]]
    # print(np.size(force_q))
    # print(np.size(unzoomedAcc))
    # exit()
    corrVel = autocorrelation(realVel)
    add_forces = [sum(x) for x in zip(force_q, realAcc)]
    corrV_AccPforce = correlation(realVel, add_forces)
    #corrVelAcc = 
    trajectory = []

#plt.plot([t*newdt for t in range(len(corrAcc))],corrAcc, label='Acc')
#plt.plot([t*newdt for t in range(len(corrVel2))],corrVel2, label='Vel')

plt.plot([t*newdt for t in range(len(corrV_AccPforce))],corrV_AccPforce, label='<v(0)(a(t)+f(t))>')

plt.plot([t*newdt for t in range(len(corrVel))],corrVel, label='<v(0)v(t)>')

plt.xlabel('t [ps]')
plt.ylabel('C(t)')

plt.legend()

plt.show()

gamma = - corrV_AccPforce/corrVel

plt.plot([t*newdt for t in range(len(gamma))],gamma, label='gamma')

plt.xlabel('t [ps]')
plt.ylabel('friction [ps^-1]')

plt.legend()

plt.show()

for i in range(numberOfTraj):
    trajectory = np.loadtxt(inputfile, skiprows=int(nLine)*i, max_rows=int(nLine)+1)

    unzoomedPos = [x for x in trajectory]
    unzoomedVel = [(trajectory[i+1*unzoomedFactor,1]-trajectory[i-1*unzoomedFactor,1])/(2.*dt*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    unzoomedAcc = [(trajectory[i+1*unzoomedFactor,1]-2.*trajectory[i,1]+trajectory[i-1*unzoomedFactor,1])/(dt*dt*unzoomedFactor*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    #unzoomedVel = [(trajectory[1,1]-trajectory[0,1])/dt] + unzoomedVel + [(trajectory[-1,1]-trajectory[-2,1])/dt] 
    # matrixXAC.append(autocorrelation(trajectory[::unzoomedFactor,1]))
    # matrixVAC.append(autocorrelation(unzoomedVel))

    # matrixXAC.append(autocorrelationFFT(trajectory[::unzoomedFactor,1]))
    # matrixVAC.append(autocorrelationFFT(unzoomedVel))

    # matrixXAC.append(signal.correlate(trajectory[::unzoomedFactor,1],trajectory[::unzoomedFactor,1]))
    # matrixVAC.append(signal.correlate(unzoomedVel,unzoomedVel))
    # corrVel = autocorrelation(unzoomedVel)
    # corrVel2 = correlation(unzoomedVel,unzoomedVel)
    #corrAcc = autocorrelation(unzoomedAcc)
    realAcc = [a for a in trajectory[:,3]]
    #realAcc = np.zeros(len(unzoomedVel))
    #realVel = [v for v in trajectory[1:-1,2]]
    realVel = [v for v in trajectory[1:-1,2]]
    dFdq_t= [dFdq(x) for x in trajectory[1:-1,1]] 

    force_q = [-dFdq(x)/mass for x in trajectory[1:-1,1]]
    # print(np.size(force_q))
    # print(np.size(unzoomedAcc))
    # exit()
    corrVel = autocorrelation(unzoomedVel)
    add_forces = [sum(x) for x in zip(force_q, unzoomedAcc)]
    corrV_AccPforce = correlation(unzoomedVel, add_forces)
    #corrVelAcc = 
    trajectory = []

#plt.plot([t*newdt for t in range(len(corrAcc))],corrAcc, label='Acc')
#plt.plot([t*newdt for t in range(len(corrVel2))],corrVel2, label='Vel')

plt.plot([t*newdt for t in range(len(corrV_AccPforce))],corrV_AccPforce, label='<v(0)(a(t)+f(t))>')

plt.plot([t*newdt for t in range(len(corrVel))],corrVel, label='<v(0)v(t)>')

plt.xlabel('t [ps]')
plt.ylabel('C(t)')

plt.legend()

plt.show()

gamma = - corrV_AccPforce/corrVel

plt.plot([t*newdt for t in range(len(gamma))],gamma, label='gamma')

plt.xlabel('t [ps]')
plt.ylabel('friction [ps^-1]')

plt.legend()

plt.show()