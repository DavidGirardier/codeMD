import numpy as np

# numberAtoms = 864
# numberIni = 984
# numberAu = 144
# numberPhS = 60

numberAtoms = 630
numberIni = 718
numberAu = 102
numberPhS = 44


new_index = []
counter = 0
counter_mol = 0
to_delete = []
for i in range(numberIni):
     
    counter = counter + 1
    counter_mol = counter_mol + 1
    if counter < (numberIni-numberAu):
        if counter_mol == 9 :
            to_delete.append(counter)

        elif counter_mol == 10 :
            to_delete.append(counter)
            
        else :

            new_index.append(counter)
        if counter_mol == 14:
            counter_mol = 0

    else:
        new_index.append(counter)
    
def modify_columns(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        modifier = "none"
        for line in infile:
            print(line)
            columns = line.split()
            #print(columns)
            #print((line.strip().startswith(';')))
            lineType = True if ('atoms' in columns) or ('bonds' in columns) or ('pairs' in columns) or ('angles' in columns) or ('dihedrals' in columns) else False
            #print(columns[0])
            if (modifier == "atoms") and (not(line.strip().startswith(';')) and line.strip() != "") and not(lineType):
                if (int(columns[0]) in new_index):
                    index_mod = new_index.index(int(columns[0]))
                    columns[0] = str(int(index_mod)+1)
                    columns[5] = str(int(index_mod)+1)
                    if columns[1] == 'C':
                        columns[1] = 'HA'
                        columns[4] = 'HA1'
                        columns[7] = '1.008'
                        columns[6] = '0.130274'



                    if columns[4] == 'S':
                        columns[6] = '-0.303930'
                    if columns[4] == 'CZ':
                        columns[6] = '0.192147'
                    if columns[4] == 'CA':
                        columns[6] = '-0.095213'
                    if columns[4] == 'CD1' or columns[4] == 'CD2':
                        columns[6] = '-0.070720'
                    if columns[4] == 'CB1' or columns[4] == 'CB2':
                        columns[6] = '-0.180892'
                    if columns[4] == 'HD1' or columns[4] == 'HB2': #close from S
                        columns[6] = '0.142225'
                    if columns[4] == 'HB1' or columns[4] == 'HD2': #far from S
                        columns[6] = '0.147748'
                    outfile.write("\t".join(columns) + "\n")
                

                
            
            elif (modifier == "bonds") and (not(line.strip().startswith(';')) and line.strip() != "") and not(lineType):
                if (int(columns[0]) in new_index) and (int(columns[1]) in new_index) :
                    index_mod = new_index.index(int(columns[0]))
                    columns[0] = str(int(index_mod)+1)
                    index_mod = new_index.index(int(columns[1]))
                    columns[1] = str(int(index_mod)+1)
                    outfile.write("\t".join(columns) + "\n")

            elif (modifier == "pairs") and (not(line.strip().startswith(';')) and line.strip() != "") and not(lineType):
                if (int(columns[0]) in new_index) and (int(columns[1]) in new_index) :
                    index_mod = new_index.index(int(columns[0]))
                    columns[0] = str(int(index_mod)+1)
                    index_mod = new_index.index(int(columns[1]))
                    columns[1] = str(int(index_mod)+1)
                    outfile.write("\t".join(columns) + "\n")

            elif (modifier == "angles") and (not(line.strip().startswith(';')) and line.strip() != "") and not(lineType):
                if (int(columns[0]) in new_index) and (int(columns[1]) in new_index) and (int(columns[2]) in new_index) :
                    index_mod = new_index.index(int(columns[0]))
                    columns[0] = str(int(index_mod)+1)
                    index_mod = new_index.index(int(columns[1]))
                    columns[1] = str(int(index_mod)+1)
                    index_mod = new_index.index(int(columns[2]))
                    columns[2] = str(int(index_mod)+1)
                    outfile.write("\t".join(columns) + "\n")
            
            elif (modifier == "dihedrals") and (not(line.strip().startswith(';')) and line.strip() != "") and not(lineType):
                if (int(columns[0]) in new_index) and (int(columns[1]) in new_index) and (int(columns[2]) in new_index) and (int(columns[3]) in new_index) :
                    index_mod = new_index.index(int(columns[0]))
                    columns[0] = str(int(index_mod)+1)
                    index_mod = new_index.index(int(columns[1]))
                    columns[1] = str(int(index_mod)+1)
                    index_mod = new_index.index(int(columns[2]))
                    columns[2] = str(int(index_mod)+1)
                    index_mod = new_index.index(int(columns[3]))
                    columns[3] = str(int(index_mod)+1)
                    outfile.write("\t".join(columns) + "\n")

            else :
                outfile.write(line)

            #print(columns)
            if 'atoms' in columns:
                modifier = "atoms"
            if 'bonds' in columns:
                modifier = "bonds"
            if 'pairs' in columns:
                modifier = "pairs"
            if 'angles' in columns:
                modifier = "angles"
            if 'dihedrals' in columns:
                modifier = "dihedrals"
            #print(modifier)
                

input_file = 'au102_pmba44.itp'  
output_file = 'au102_phs44.itp'  

modify_columns(input_file, output_file)