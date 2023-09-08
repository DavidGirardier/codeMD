import numpy as np
# Function to make a number positive if it's smaller than -2
def make_positive_if_smaller_than_minus_2(value):
    if value < -2:
        return value + 2.0*np.pi
    else:
        return value

# Input and output file names
input_file_name = "100shooting"
output_file_name = input_file_name+ "_modif"

# Open the input file for reading
try:
    with open(input_file_name, 'r') as input_file:
        # Read lines from the input file
        lines = input_file.readlines()
except FileNotFoundError:
    print(f"Error: File '{input_file_name}' not found.")
    exit(1)

# Create a list to store modified lines
modified_lines = []

# Process each line from the input file
for line in lines:
    # Split each line into two columns
    columns = line.strip().split()
    
    # Check if there are exactly two columns
    if len(columns) == 2:
        try:
            # Convert the second column to a float and apply the transformation
            column2_value = float(columns[1])
            modified_value = make_positive_if_smaller_than_minus_2(column2_value)
            
            # Append the modified line to the list
            modified_line = f"{columns[0]}\t{modified_value}\n"
            modified_lines.append(modified_line)
        except ValueError:
            # Handle the case where the second column is not a valid float
            print(f"Warning: Skipping line due to invalid value - {line}")
    else:
        # Handle the case where the line doesn't have exactly two columns
        print(f"Warning: Skipping line with incorrect format - {line}")

# Write the modified lines to the output file
with open(output_file_name, 'w') as output_file:
    output_file.writelines(modified_lines)

print(f"File '{output_file_name}' has been created with modified values.")
