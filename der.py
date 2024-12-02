import numpy as np
import glob

def read_file(file_path):
    # Read the file into a numpy array
    data = np.loadtxt(file_path)
    return data

def compute_derivative(data):
    # Compute the derivative of the second column with respect to the first column
    x = data[::2, 0]
    y = data[::2, 1]
    dy_dx = np.gradient(y, x)
    return x, dy_dx

def save_to_file(x, dy_dx, output_file_path):
    # Save the result to a file
    result = np.column_stack((x, dy_dx))
    np.savetxt(output_file_path, result, fmt='%.6f', delimiter='\t', header='x\tdy_dx', comments='')

def main(input_file, output_file):
    data = read_file(input_file)
    x, dy_dx = compute_derivative(data)
    save_to_file(x, dy_dx, output_file)
    print(f"Derivative saved to {output_file}")

# Example usage
all_files = glob.glob('Log*')
for i in all_files:
    input_file = i  # Replace with your input file path
    output_file = 'der_'+input_file  # Replace with your output file path
    main(input_file, output_file)
