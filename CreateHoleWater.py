import numpy as np

filename = 'minimized_box_water.data'
filename = 'minimized_box_water.data'
radius = 5.0

statusAtom = False
listMoltoDelete = []
with open(filename, 'r') as file:
    lines = file.readlines()
    
    
    for line in lines[1:]:

        splitted = line.split()
        
        if len(splitted)>0:
            
            if splitted[0] == 'Velocities':
                
                break

            if statusAtom == True :
                position = [float(i) for i in splitted[4:7]]
                #print(position)
                if (np.sqrt(position[0]**2 + position[1]**2 + position[2]**2)<= radius):
                    listMoltoDelete.append(splitted[1])
            
            if splitted[0] == 'Atoms' :
                statusAtom = True

line_to_delete = []
atom_to_delete = []       
counter=0 
status = 'None'
num_Atoms = 0     
num_Bonds = 0     
num_Angles = 0     
    
with open(filename, 'r') as file:
    
    for line in lines[1:]:

        counter+=1

        lines = file.readlines()                
        splitted = line.split()
        

        if len(splitted)>0:

            
            if len(splitted)>1:
                if status == 'StatusAtoms' :
                        
                    if splitted[1] in listMoltoDelete:
                        line_to_delete.append(counter)
                        atom_to_delete.append(splitted[1])
                        num_Atoms += 1

                if status == 'StatusVel' :
                        
                    if splitted[0] in atom_to_delete:
                        line_to_delete.append(counter)
                
                if status == 'StatusBonds' :
                        
                    if (splitted[2] in atom_to_delete) or (splitted[3] in atom_to_delete):
                        line_to_delete.append(counter)
                        num_Bonds += 1

                if status == 'StatusAngles' :
                        
                    if (splitted[2] in atom_to_delete) or (splitted[3] in atom_to_delete) or (splitted[4] in atom_to_delete):
                        line_to_delete.append(counter)    
                        num_Angles += 1
                
            if splitted[0] == 'Atoms' :
                status = 'StatusAtoms'
            
            if splitted[0] == 'Velocities':              
                status = 'StatusVel'

            if splitted[0] == 'Bonds':              
                status = 'StatusBonds'
                       
            if splitted[0] == 'Angles':              
                status = 'StatusAngles'

            if splitted[0] == 'Impropers':              
                status = 'StatusImpropers'


with open(filename, 'r') as file:
    lines = file.readlines()

print(lines)
with open("new"+filename, 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        splitted = line.split()
        if (number+1) not in line_to_delete:
             
            if len(splitted) > 1:
                
                if splitted[1]== 'atoms':
                    fp.write(str(int(splitted[0])-num_Atoms) + ' atoms\n')
                
                elif splitted[1]== 'bonds':
                    fp.write(str(int(splitted[0])-num_Bonds) + ' bonds\n')
                
                elif splitted[1]== 'angles':
                    fp.write(str(int(splitted[0])-num_Atoms) + ' angles\n')

                else :
                    fp.write(line)
            else :
                fp.write(line)
              

print(atom_to_delete)
print(listMoltoDelete)

    
    