import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pot import Z1,Z2,Z3,Z4
from integratorsULE import EulerMaruyama


import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
# 1) Parameters & single long run (ergodic trajectory)
# --------------------------------------------------------------------
pot = Z4    # e.g. your potential parameter
m   = 1.0
g   = 1.0
kT  = 1.0
pos0 = [0.0, 0.0]
dt    = 0.001
tot_t = 100000

# Suppose EulerMaruyama returns t_array, x_array, y_array
# each of length nsteps
vel0x = np.sqrt(kT/m) * np.random.normal()
vel0y = np.sqrt(kT/m) * np.random.normal()

t_array, x_array, y_array = EulerMaruyama(
    m, g, kT, pos0, [vel0x, vel0y],
    dt, tot_t, pot
)

# Convert to NumPy arrays (if not already)
t_array = np.array(t_array)
x_array = np.array(x_array)
y_array = np.array(y_array)

nsteps_total = len(t_array)
print("Trajectory length:", nsteps_total)

# --------------------------------------------------------------------
# 2) Define the bin centers / widths and the time lag
# --------------------------------------------------------------------
x0, y0 = 0.0, 0.0      # "initial" condition of interest
bin_width_x = 0.2
bin_width_y = 0.2

Delta_t = 1.0
time_step = t_array[1] - t_array[0] 
Delta_n = int(Delta_t / time_step)
print(f"time_step = {time_step}, Delta_n = {Delta_n}")

# --------------------------------------------------------------------
# 3) Find indices for each condition
# --------------------------------------------------------------------
indices_xy = []   # for (X(0) ~ x0, Y(0) ~ y0)
indices_x  = []   # for (X(0) ~ x0) only
indices_y  = []   # for (Y(0) ~ y0) only

half_bin_x = bin_width_x/2
half_bin_y = bin_width_y/2

for n in range(nsteps_total - Delta_n):
    # Condition for X(0)=x0, Y(0)=y0
    if (abs(x_array[n] - x0) < half_bin_x) and (abs(y_array[n] - y0) < half_bin_y):
        indices_xy.append(n)

    # Condition for X(0)=x0 only
    if abs(x_array[n] - x0) < half_bin_x:
        indices_x.append(n)

    # Condition for Y(0)=y0 only
    if abs(y_array[n] - y0) < half_bin_y:
        indices_y.append(n)

indices_xy = np.array(indices_xy, dtype=int)
indices_x  = np.array(indices_x,  dtype=int)
indices_y  = np.array(indices_y,  dtype=int)

print("Number of (x,y) matches:", len(indices_xy))
print("Number of x-only matches:", len(indices_x))
print("Number of y-only matches:", len(indices_y))

# --------------------------------------------------------------------
# 4) Collect future values: X(t0+Delta_t) and Y(t0+Delta_t)
# --------------------------------------------------------------------
# Full conditioning
x_future_xy = x_array[indices_xy + Delta_n]
y_future_xy = y_array[indices_xy + Delta_n]

# Partial conditioning: only X(0) ~ x0
x_future_x = x_array[indices_x + Delta_n]

# Partial conditioning: only Y(0) ~ y0
y_future_y = y_array[indices_y + Delta_n]

# --------------------------------------------------------------------
# 5) Plot
# --------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# -- LEFT subplot: distributions of X(t)
ax1.hist(x_future_xy, bins=40, density=True, alpha=0.5, color='blue',
         label='X(t) | X(0)=x0 & Y(0)=y0')
ax1.hist(x_future_x, bins=40, density=True, alpha=0.5, color='green',
         label='X(t) | X(0)=x0 only')
ax1.set_title(f"Distribution of X(t0+{Delta_t})\nComparing full vs. partial conditioning")
ax1.set_xlabel("X position at t0+Δt")
ax1.set_ylabel("Probability density")
ax1.legend()

# -- RIGHT subplot: distributions of Y(t)
ax2.hist(y_future_xy, bins=40, density=True, alpha=0.5, color='red',
         label='Y(t) | X(0)=x0 & Y(0)=y0')
ax2.hist(y_future_y, bins=40, density=True, alpha=0.5, color='orange',
         label='Y(t) | Y(0)=y0 only')
ax2.set_title(f"Distribution of Y(t0+{Delta_t})\nComparing full vs. partial conditioning")
ax2.set_xlabel("Y position at t0+Δt")
ax2.set_ylabel("Probability density")
ax2.legend()

plt.tight_layout()
plt.show()
