# Define file paths
input_file = "disso.gro"  # Change this to the path of your input .gro file
output_file = "dissoXY.gro"  # Change this to your desired output file path

# Define atom index ranges
first_nanoparticle_range = range(1, 865)  # Atoms 1 to 864
second_nanoparticle_range = range(865, 1729)  # Atoms 865 to 1728

# Read the .gro file and modify atom names
with open(input_file, "r") as file:
    lines = file.readlines()

# Open output file to write modified lines
with open(output_file, "w") as file:
    for line in lines[2:]:
        # Check if it's a line with atom information (assuming it's longer than 20 chars)
        if len(line) > 20:
            atom_index = int(line[15:20].strip())  # Extract atom index
            atom_name = line[10:15].strip()        # Extract atom name
            
            # Replace atom names based on index ranges and atom names
            if atom_index in first_nanoparticle_range and atom_name in ["CZ", "CD1", "CA", "CB1", "CB2", "CD2"]:
                modified_line = line[:10] + "    X" + line[15:]
            elif atom_index in second_nanoparticle_range and atom_name in ["CZ", "CD1", "CA", "CB1", "CB2", "CD2"]:
                modified_line = line[:10] + "    Y" + line[15:]
            else:
                modified_line = line
        else:
            modified_line = line  # Copy header/footer lines as is

        # Write the modified line to output
        file.write(modified_line)

print("File modified and saved as", output_file)

