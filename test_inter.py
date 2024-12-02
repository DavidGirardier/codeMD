import numpy as np

# Define your data
data = """
0.00000000e+00 0.00000000e+00
1.63539375e-02 1.00000000e-01
2.92709458e-02 2.00000000e-01
3.66017804e-02 1.00000000e-01
3.72587179e-02 2.00000000e-01
4.22254966e-02 1.00000000e-01
4.35362319e-02 2.00000000e-01
4.92312588e-02 3.00000000e-01
5.58026728e-02 4.00000000e-01
6.11009074e-02 5.00000000e-01
6.50222623e-02 6.00000000e-01
7.31785036e-02 5.00000000e-01
7.68398459e-02 4.00000000e-01
7.84555196e-02 5.00000000e-01
8.30800500e-02 6.00000000e-01
8.58856319e-02 5.00000000e-01
9.26787214e-02 4.00000000e-01
9.52212466e-02 3.00000000e-01
"""

# Convert the data to a numpy array
from io import StringIO
data_array = np.loadtxt(StringIO(data))

# Extract time and position columns
time = data_array[:, 0]
position = data_array[:, 1]

# Define the fixed time steps
fixed_time_steps = np.arange(start=0, stop=time.max(), step=0.0001)

# Create a function to find the last known position at each fixed time step
def interpolate_position_at_fixed_times(times, positions, new_times):
    # Initialize the result array
    new_positions = np.zeros_like(new_times)
    j = 0
    for i, t in enumerate(new_times):
        while j < len(times) and times[j] <= t:
            j += 1
        new_positions[i] = positions[j - 1] if j > 0 else positions[0]
    return new_positions

# Get the new interpolated positions
fixed_positions = interpolate_position_at_fixed_times(time, position, fixed_time_steps)

# Combine the fixed time steps and positions into a single array
fixed_trajectory = np.column_stack((fixed_time_steps, fixed_positions))

# Save the numpy array to a file
np.save('fixed_trajectory.npy', fixed_trajectory)

# Print the result for verification
print(fixed_trajectory)
