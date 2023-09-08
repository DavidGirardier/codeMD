import numpy as np
import matplotlib.pyplot as plt

# Define function to compute derivative
def derivative(x, y):
    return np.gradient(y, x)

# Define filenames and corresponding labels
filenames = ["Profg3_27m147_67_fraction500colvar_c60_precise_newdt0_2_" + str(x) for x in range(1,6)]
labels = ["set 1", "set 2", "set 3", "set 4" , "set 5"]

legends = labels

# Initialize figure
fig, axs = plt.subplots(2, 1)

# Loop over files and plot curves on first axis
for i, filename in enumerate(filenames):
    # Load data from file
    data = np.loadtxt(filename)
    x = data[:, 0]
    y = data[:, 1]
    
    # Filter data between x = 0.9 and 1.6
    mask = np.logical_and(x >= 0.9, x <= 1.4)
    x = x[mask]
    y = y[mask]
    
    # Plot curve
    axs[0].plot(x, y, label=labels[i])
    axs[0].set_xlabel("q")
    axs[0].set_ylabel("F")
    axs[0].set_title("Curves")
    axs[0].legend()

# Loop over files again and plot derivatives on second axis
counter = 0
for i, filename in enumerate(filenames):
    # Load data from file
    counter = counter + 1
    data = np.loadtxt(filename)
    x = data[:, 0]
    y = data[:, 1]
    
    # Filter data between x = 0.9 and 1.6
    mask = np.logical_and(x >= 0.9, x <= 1.4)
    x = x[mask]
    y = y[mask]
    
    # Compute derivative
    dydx = derivative(x, y)
    
    # Plot derivative
    axs[1].plot(x, dydx, label=legends[i])
    axs[1].set_xlabel("q")
    axs[1].set_ylabel("dF/dq")
    axs[1].set_title("Derivatives")
    axs[1].legend()

    outputName = 'Derivt20ps_' + str(int(i))
    np.savetxt(outputName, np.c_[x,dydx], fmt='%1.8E')

# Adjust layout and show plot
plt.tight_layout()
plt.show()