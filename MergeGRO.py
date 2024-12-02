def process_files(file1_path, file2_path, output_path):
    # Open both files and read their contents
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
    
    # Initialize variables to store frame-related information
    frames1 = {}
    frames2 = []
    
    # Process file1 to extract "61CLU" lines based on frames
    current_frame = None
    for line in lines1:
        if line.startswith("frame"):
            current_frame = line.strip()  # Store the current frame header
        elif "61CLU" in line and current_frame is not None:
            # Store the "61CLU" line associated with the current frame
            frames1[current_frame] = line.strip()

    # Process file2 to insert "61CLU" lines after the exact match of "115593"
    current_frame = None
    updated_lines2 = []
    for line in lines2:
        updated_lines2.append(line.strip())  # Add each line to the output list
        if line.startswith("frame"):
            current_frame = line.strip()  # Track the current frame header
        # Check if the line is exactly "115593" (ignoring leading/trailing spaces)
        if line.strip() == "115593" and current_frame in frames1:
            # Replace "115593" with "115594" and append to output
            updated_lines2[-1] = line.replace("115593", "115594").strip()
            # Insert the corresponding "61CLU" line after "115594"
            updated_lines2.append(frames1[current_frame])

    # Write the updated content to the output file
    with open(output_path, 'w') as output_file:
        for line in updated_lines2:
            output_file.write(line + '\n')



# File paths
file1 = 'com.gro'  # Replace with your actual file path for file 1
file2 = 'traj.gro'  # Replace with your actual file path for file 2
output_file = 'combined.gro'  # Output file path

# Run the processing function
process_files(file1, file2, output_file)
