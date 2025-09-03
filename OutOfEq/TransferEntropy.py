import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pot import Z1,Z2,Z3
from integratorsULE import EulerMaruyama


pot=Z3   
ntraj=1000
m = 1.
g = 1.
kT = 1.
pos0 = [0.,0.]
dt=0.001
tot_t=100
ev=1

all_t = []
all_x = []
all_y = []

pos_x_all = []
pos_x2_all = []
pos_y_all = []
pos_y2_all = []

for i in range(ntraj):
    vel0x = np.sqrt(kT/m) * np.random.normal()
    vel0y = np.sqrt(kT/m) * np.random.normal()
    
    t, pos_x, pos_y = EulerMaruyama(m, g, kT, pos0, [vel0x, vel0y], dt, tot_t, pot)
    plt.plot(pos_x,pos_y,'-')
    pos_x_all.append(pos_x)
    pos_y_all.append(pos_y)
plt.show()
pos0 = [0.5,0.]
exit()
# Convert to arrays of shape (ntraj, nsteps)
pos_x_all = np.array(pos_x_all)  
pos_y_all = np.array(pos_y_all)

for i in range(ntraj):
    vel0x = np.sqrt(kT/m) * np.random.normal()
    vel0y = np.sqrt(kT/m) * np.random.normal()
    
    t, pos_x, pos_y = EulerMaruyama(m, g, kT, pos0, [vel0x, vel0y], dt, tot_t, pot)
    

    pos_y2_all.append(pos_y)

pos0 = [0.,0.5]

# Convert to arrays of shape (ntraj, nsteps)
pos_x_all = np.array(pos_x_all)  
pos_y_all = np.array(pos_y_all)

for i in range(ntraj):
    vel0x = np.sqrt(kT/m) * np.random.normal()
    vel0y = np.sqrt(kT/m) * np.random.normal()
    
    t, pos_x, pos_y = EulerMaruyama(m, g, kT, pos0, [vel0x, vel0y], dt, tot_t, pot)
    
    pos_x2_all.append(pos_x)



# Convert to arrays of shape (ntraj, nsteps)
pos_x2_all = np.array(pos_x2_all)  
pos_y2_all = np.array(pos_y2_all)  


import matplotlib.pyplot as plt

nsteps = len(t)  # total number of time steps

# Example: pick a few time points to visualize
time_indices = [0, nsteps//4, nsteps//2, 3*nsteps//4, nsteps-1]

# for k in time_indices:
#     plt.figure()
    
#     # Extract the x-values at time index k across all ntraj
#     xvals = pos_x_all[:, k]
#     x2vals = pos_x2_all[:, k]
#     yvals = pos_y_all[:, k]
#     y2vals = pos_y2_all[:, k]
    
#     # Plot histograms
#     plt.hist(yvals, bins=50, alpha=0.5, density=True, label='Y distribution')
#     plt.hist(y2vals, bins=50, alpha=0.5, density=True, label='Y2 distribution')
#     plt.hist(xvals, bins=50, alpha=0.5, density=True, label='X distribution')
#     plt.hist(x2vals, bins=50, alpha=0.5, density=True, label='X2 distribution')

#     plt.title(f'Distributions at time = {t[k]:.2f}')
#     plt.legend()
#     plt.show()

# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Suppose you have the EulerMaruyama function:
# def EulerMaruyama(m, g, kT, pos0, vel0, dt, tot_t, Z1):
#    ...
#    return t_array, x_array, y_array

# ------------------------
# Parameters (example)
# ------------------------
m = 1.0
g = 1.0
kT = 1.0
x0 = 0.0          # we'll fix X(0) = 0 for all runs
y0_values = [0., 0.25, 0.5, 1.]  # four different Y(0) values to demonstrate the effect
ntraj = 10000       # number of trajectories for each Y(0)
dt = 0.001
tot_t = 0.01
         # some parameter in your model, presumably

# We'll store final X positions in a dictionary keyed by Y(0) value
final_positions = {}

# ------------------------
# Simulations
# ------------------------
for y0 in y0_values:
    # List to store final X for all trajectories that start with Y(0)=y0
    x_final_list = []
    
    for i in range(ntraj):
        pos0=[x0,y0]
        vel0x = np.sqrt(kT/m) * np.random.normal()
        vel0y = np.sqrt(kT/m) * np.random.normal()
        
        # Run the Langevin integrator
        t_array, x_array, y_array = EulerMaruyama(m, g, kT, pos0, [vel0x, vel0y], dt, tot_t, pot)
        
        # We'll just take the final position of x_array
        x_final = x_array[-1]
        x_final_list.append(x_final)
    
    final_positions[y0] = np.array(x_final_list)

# ------------------------
# Plot overlapping histograms
# ------------------------
plt.figure(figsize=(7,5))

for y0 in y0_values:
    data = final_positions[y0]
    plt.hist(
        data, bins=50, density=True, alpha=0.5,
        label=f"Y(0) = {y0}"
    )

plt.xlabel("X at final time")
plt.ylabel("Probability density")
plt.title("Final X distribution for different Y(0)")
plt.legend()
plt.show()

y0 = 0.0          # we'll fix X(0) = 0 for all runs
x0_values = [0., 0.25, 0.5, 1.]  # four different Y(0) values to demonstrate the effect

         # some parameter in your model, presumably

# We'll store final X positions in a dictionary keyed by Y(0) value
final_positions = {}

# ------------------------
# Simulations
# ------------------------
for x0 in x0_values:
    # List to store final X for all trajectories that start with Y(0)=y0
    y_final_list = []
    
    for i in range(ntraj):
        pos0=[x0,y0]
        vel0x = np.sqrt(kT/m) * np.random.normal()
        vel0y = np.sqrt(kT/m) * np.random.normal()
        
        # Run the Langevin integrator
        t_array, x_array, y_array = EulerMaruyama(m, g, kT, pos0, [vel0x, vel0y], dt, tot_t, pot)
        
        # We'll just take the final position of x_array
        y_final = y_array[-1]
        y_final_list.append(y_final)
    
    final_positions[x0] = np.array(y_final_list)

# ------------------------
# Plot overlapping histograms
# ------------------------
plt.figure(figsize=(7,5))

for x0 in x0_values:
    data = final_positions[x0]
    plt.hist(
        data, bins=50, density=True, alpha=0.5,
        label=f"x(0) = {x0}"
    )

plt.xlabel("X at final time")
plt.ylabel("Probability density")
plt.title("Final X distribution for different Y(0)")
plt.legend()
plt.show()



exit()
bins = 50

# Calculate the 2D histogram
hist, x_edges, y_edges = np.histogram2d(pos_x, pos_y, bins=bins, range=[[-1.5, 1.5], [-1.5, 1.5]])

# Normalize the histogram
bin_area = (x_edges[1] - x_edges[0]) * (y_edges[1] - y_edges[0])  # Area of each bin
hist_normalized = hist / (len(pos_x) * bin_area)  # Normalized to probability density

# Plot the normalized histogram
plt.imshow(hist_normalized.T, origin='lower', extent=[-1.5, 1.5, -1.5, 1.5], cmap='viridis', aspect='auto')

# Add a color bar
plt.colorbar(label='Probability Density')

# Label the axes
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Normalized 2D Histogram of Particle Positions')

# Show the plot
plt.show()