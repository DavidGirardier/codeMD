import numpy as np
import matplotlib.pyplot as plt

# Load the 1D array from file
data = np.loadtxt("colvar_d_c60")
print("data shape:", data.shape)
print("data size:", data.size)
# Determine the length of each trajectory

traj_length = data.shape[1] // 2

# Reshape the array into a 2D array
trajectories = data.reshape((-1, traj_length, 2))[:,:,1]


# Plot each trajectory
for traj in trajectories:
    plt.plot(traj)



# Add labels and title
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("100 Trajectories")

# Show the plot
plt.show()
