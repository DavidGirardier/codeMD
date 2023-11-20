import numpy as np

from scipy.fftpack import fft, ifft, ifftshift

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


# inputfile = input('Trajectory File:')
# trajectories = np.loadtxt(inputfile, max_rows=2)
inputfile= 'OverdampedWithULE1'
unzoomedFactor = 1
dt = 0.0001

#dt=0.001
numberOfTraj = 1
tFile = 10000.
nLine = tFile/dt
newdt = dt * unzoomedFactor

matrixXAC = []
matrixVAC = []

for i in range(numberOfTraj):
    trajectory = np.loadtxt(inputfile, skiprows=int(nLine)*i, max_rows=int(nLine)+1)
    unzoomedPos = [x for x in trajectory]
    unzoomedVel = [(trajectory[i+1*unzoomedFactor,1]-trajectory[i-1*unzoomedFactor,1])/(2.*dt*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    #unzoomedVel = [(trajectory[1,1]-trajectory[0,1])/dt] + unzoomedVel + [(trajectory[-1,1]-trajectory[-2,1])/dt] 
    #matrixXAC.append(autocorrelation(trajectory[::unzoomedFactor,1]))
    #matrixVAC.append(autocorrelation(unzoomedVel))

    matrixXAC.append(autocorrelationFFT(trajectory[::unzoomedFactor,1]))
    matrixVAC.append(autocorrelationFFT(unzoomedVel))

    # matrixXAC.append(signal.correlate(trajectory[::unzoomedFactor,1],trajectory[::unzoomedFactor,1]))
    # matrixVAC.append(signal.correlate(unzoomedVel,unzoomedVel))
    
    trajectory = []

print(matrixXAC)
print([matrixXAC[i][-1] for i in range(numberOfTraj)])
print(np.var([matrixXAC[i][-1] for i in range(numberOfTraj)]))
XAC = np.mean(matrixXAC, axis=0)
VAC = np.mean(matrixVAC, axis=0)
XACvariance = np.var(matrixXAC, axis=0)
VACvariance = np.var(matrixVAC, axis=0)
#np.savetxt(outputName, np.c_[[t*newdt for t in range(int(tFile/newdt) + 1)], XAC, VAC], fmt='%1.8E')
outputName='VAC'+inputfile+'unzoomed'+str(unzoomedFactor)
np.savetxt(outputName, np.c_[[t*newdt for t in range(len(VAC))], VAC, VACvariance/np.sqrt(numberOfTraj)], fmt='%1.8E')

outputName='XAC'+inputfile+'unzoomed'+str(unzoomedFactor)
np.savetxt(outputName, np.c_[[t*newdt for t in range(len(XAC))], XAC, XACvariance/np.sqrt(numberOfTraj)], fmt='%1.8E')
#np.savetxt(outputName, np.c_[XAC, VAC], fmt='%1.8E')
print(inputfile+'unzoomed'+str(unzoomedFactor))
#print(np.mean([[2,2], [1,1]], axis=0))

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the function to fit
def funcPos(x, g, w):
    #return np.exp(-g*x)*(np.cos(np.sqrt(w*w-g*g)*x) + g*np.sin(np.sqrt(w*w-g*g)*x)/(np.sqrt(w*w-g*g)))+d
    #return np.exp(-g*x)*(a*np.cos(w*x) + b*np.sin(w*x))+d 
    return np.exp(-g*x/2.)*(np.cos(np.sqrt(w*w-g*g/4.)*x) + (g/(2.*np.sqrt(w*w-g*g/4.)))\
            *np.sin(np.sqrt(w*w-g*g/4.)*x))
    #return np.exp(-g*x/2.)*(np.cos(np.sqrt(w*w-g*g/4.)*x) - (g/(2.*np.sqrt(w*w-g*g/4.)))\
            #*np.sin(np.sqrt(w*w-g*g/4.)*x))
    #return np.exp(-g*x)+d
def funcVel(x, g, w):
    #return np.exp(-g*x)*(np.cos(np.sqrt(w*w-g*g)*x) + g*np.sin(np.sqrt(w*w-g*g)*x)/(np.sqrt(w*w-g*g)))+d
    #return np.exp(-g*x)*(a*np.cos(w*x) + b*np.sin(w*x))+d 
    return np.exp(-g*x/2.)*(np.cos(np.sqrt(w*w-g*g/4.)*x) - (g/(2.*np.sqrt(w*w-g*g/4.)))\
            *np.sin(np.sqrt(w*w-g*g/4.)*x))

inputname = inputfile+'unzoomed'+str(unzoomedFactor)
# Load the data from a file
dt=0.0001
tmax=10.
nLine = int(tmax/dt)


data = np.loadtxt('XAC'+inputname, max_rows=int(nLine)+1)

# Separate x and y data
x = data[:, 0]
y = data[:, 1]

# Fit the curve to the function
popt, pcov = curve_fit(funcPos, x, y, p0=[5.,8.])

# Generate the fitted curve
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = funcPos(x_fit, *popt)

# Plot the original and fitted curves

plt.subplot(2, 1, 1)
plt.plot(x, y, label='MD data')
plt.plot(x_fit, y_fit, label='Fit, g =' +str((round(popt[0],2))) + ', w =' +str((round(popt[1],2))))
plt.xlabel('t [ps]')
plt.ylabel('Cx(t)')
plt.title(inputname)
plt.legend()


# Print the optimized values of a and b
print("g =", popt[0])
print("w =", popt[1])

data = np.loadtxt('VAC' + inputname, max_rows=int(nLine)+1)

# Separate x and y data
x = data[:, 0]
y = data[:, 1]

# Fit the curve to the function
popt, pcov = curve_fit(funcVel, x, y, p0=[4.,8.])
# Generate the fitted curve
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = funcVel(x_fit, *popt)

# Plot the original and fitted curves
plt.subplot(2, 1, 2)
plt.plot(x, y, label='MD data')
plt.plot(x_fit, y_fit, label='Fit, g =' +str((round(popt[0],2))) + ', w =' +str((round(popt[1],2))))
plt.xlabel('t [ps]')
plt.ylabel('Cv(t)')
plt.legend()

plt.subplots_adjust(hspace=0.5)

plt.show()

# Print the optimized values of a and b
print("g =", popt[0])
print("w =", popt[1])



