import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(trajectory_file, bins_choice ):
    # Read the trajectory file and extract values from the second column
    values = []

    if bins_choice == 'auto':
        with open(trajectory_file, 'r') as file:
            for line in file:
                columns = line.strip().split()
                if len(columns) >= 2:
                    value = float(columns[1])
                    values.append(value)

        # Plot the histogram
        plt.hist(values, bins='auto')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram of Values')
        plt.show()
    else:

        values = []
        with open(trajectory_file, 'r') as file:
            for line in file:
                columns = line.strip().split()
                if len(columns) >= 2:
                    value = float(columns[1])
                    values.append(value)

        # Plot the histogram with custom bin size
        plt.hist(values, bins=np.arange(min(values), max(values) + bins_choice, bins_choice))
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram of Values')
        plt.show()

# Provide the path to your trajectory file here
trajectory_file = 'path/to/trajectory.txt'

# Specify the desired bin size



# Provide the path to your trajectory file here
#trajectory_file = '500colvar_c60_precise'
#trajectory_file = '500colvar_c60_precise_newdt0_2'
trajectory_file = '500colvar_c60_precise_newdt0_2newt10_newdt0_2'
plot_histogram(trajectory_file, 0.01)