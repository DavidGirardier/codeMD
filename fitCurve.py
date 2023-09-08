import numpy as np
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

inputname ='colvarWell_k50000_1nsunzoomed1'
# Load the data from a file
dt=0.001
tmax=1.
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
popt, pcov = curve_fit(funcVel, x, y, p0=[5.,8.])

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

