# Hummer 2005 Position dependent diffusion
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, ifftshift
import scipy.integrate as integrate

def autocorrelation(data):
    
    x = np.array(data) 

    # Mean
    mean = np.mean(data)

    # Variance
    var = np.var(data)

    # Normalized data
    ndata = data - mean

    acorr = np.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
    acorr = acorr / var / len(ndata)

    return acorr


def autocorrelationFFT(x):
    xp = ifftshift((x - np.average(x))/np.std(x))
    n, = xp.shape
    xp = np.r_[xp[:n//2], np.zeros_like(xp), xp[n//2:]]
    f = fft(xp)
    p = np.absolute(f)**2
    pi = ifft(p)
    return np.real(pi)[:n//2]/(np.arange(n//2)[::-1]+n//2)


def diffusion(traj_time,traj):


    #return traj
    dt = traj[1,0]-traj[0,0]
    var_q = np.var(traj[:,1])

    #XAC = autocorrelation(traj[:,1])
    XAC_FFT = autocorrelationFFT(traj[:,1])

    tau_q = integrate.cumulative_trapezoid(XAC_FFT[:],traj_time[:len(XAC_FFT)])

    D_q = var_q/tau_q

    return traj[len(D_q),0], XAC_FFT, D_q



for k in ['0','500','1000','2000','5000', '10000', '20000','50000']:
    path = 'k'+str(k)+'/'
    inputfile = 'dwell_k'+str(k)
    dt = 0.001
    numberOfTraj = 10
    tFile = 10**4
    nLine = tFile/dt
    
    tmax = 100
    linemax = int(tmax/dt)
    matrixXAC = []
    matrixDiff = []
    
    for i in range(numberOfTraj):
        print(i)
        print(int(nLine)*i)
        trajectory = np.loadtxt(path+inputfile, skiprows=int(nLine)*i, max_rows=int(nLine)+1, comments='#')
        if i==0 :   
            unique_time = trajectory[:,0]
        time, XAC, diff = diffusion(unique_time,trajectory)
        matrixXAC.append(XAC[:linemax])
        matrixDiff.append(diff[:linemax])
        
    
    
    
    meanXAC = np.mean(matrixXAC, axis=0)
    errXAC = np.std(matrixXAC, axis=0)/np.sqrt(numberOfTraj)

    meanDiff = np.mean(matrixDiff, axis=0)
    errDiff = np.std(matrixDiff, axis=0)/np.sqrt(numberOfTraj)

    
#     plt.subplot(2, 1, 1)

#     #plt.errorbar(traj[:len(meanXAC),0], meanXAC, yerr=errXAC, label='XAC_k'+k)
#     plt.fill_between(unique_time[:linemax], meanXAC[:linemax]-errXAC[:linemax], meanXAC[:linemax]+errXAC[:linemax], alpha=0.5)
#     plt.plot(unique_time[:linemax], meanXAC[:linemax],label='XAC_k'+k)
    
#     plt.xlabel('t [ps]')
#     plt.ylabel('XAC(t)')
    
    
    
#     plt.legend()
    
#     plt.subplot(2, 1, 2)
    
#     plt.fill_between(unique_time[:linemax], meanDiff[:linemax]-errDiff[:linemax], meanDiff[:linemax]+errDiff[:linemax],alpha=0.5)
#     plt.plot(unique_time[:linemax], meanDiff[:linemax],label='Diffusion_k'+k)
#     plt.xlabel('t [ps]')
#     plt.ylabel('D(t)')
    
    
    
#     plt.legend()
    outputName = 'Diff'+inputfile  
    np.savetxt(outputName, np.c_[unique_time[:len(meanDiff)],meanDiff,errDiff], fmt='%1.8E')

# plt.show() 


