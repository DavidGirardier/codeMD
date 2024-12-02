import numpy as np

def compute_fluctuation(data):
    # Load the data from the txt file (assuming one column)
    

    # Compute the mean of the column
    mean_value = np.mean(data)

    # Compute the differences between each data point and the mean (fluctuation)
    differences = data - mean_value

    # Compute the standard deviation (measure of fluctuation)
    fluctuation = np.std(data)

    return differences, fluctuation

# Usage
input_file = 'cv'  # Replace this with the path to your file
data = np.loadtxt(input_file)
differences, fluctuation = compute_fluctuation(data[:,1])

# Output the results
print("Differences from the mean:")
print(differences)
print("\nFluctuation (Standard Deviation):", fluctuation)
