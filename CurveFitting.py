import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the function to fit
def func(x, a, b):
    return np.exp(b*x)*np.cos(a*x)

# Load the data from a file
data = np.loadtxt('XAC')

# Separate x and y data
x = data[:, 0]
y = data[:, 1]

# Fit the curve to the function
popt, pcov = curve_fit(func, x, y)

# Generate the fitted curve
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = func(x_fit, *popt)

# Plot the original and fitted curves
plt.plot(x, y, label='Original Curve')
plt.plot(x_fit, y_fit, label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Print the optimized values of a and b
print("a =", popt[0])
print("b =", popt[1])
