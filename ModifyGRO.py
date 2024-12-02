import numpy as np

def modify_gro_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    atom_number = 1
    new_lines = []
    
    # Copy the title and number of atoms lines as is
    new_lines.append(lines[0])  # Title
    new_lines.append(lines[1])  # Number of atoms

    # Modify the third column (atom number) of the atom lines
    for line in lines[2:]:
        if line.strip():  # Ensure it's not a blank line
            # Format of atom lines is fixed-width, so slice carefully
            # First 15 characters are for residue number, residue name, and atom name
            prefix = line[:15]
            # Replace the atom number (next 5 characters) with the new atom_number, ensuring correct spacing
            new_atom_number = f"{atom_number:5d}"
            suffix = line[20:]  # The rest (coordinates, etc.)
            new_line = f"{prefix}{new_atom_number}{suffix}"
            new_lines.append(new_line)
            atom_number += 1
    
    # Write the modified lines to the output file
    with open(output_file, 'w') as file:
        file.writelines(new_lines)

# Use the function
input_file = 'output.gro'  # Replace with your actual input file name
output_file = 'final.gro'  # Replace with your desired output file name
modify_gro_file(input_file, output_file)
