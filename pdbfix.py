with open("shoot.pdb", "r") as infile, open("fixed_shoot.pdb", "w") as outfile:
    atom_serial = 1  # Start serial numbering from 1
    for line in infile:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            # Write the line with the new atom serial number
            outfile.write(f"{line[:6]}{atom_serial:5}{line[11:]}")
            atom_serial += 1
            if atom_serial > 99999:
                atom_serial = 1

        else:
            # For non-ATOM lines, write them as-is
            outfile.write(line)
