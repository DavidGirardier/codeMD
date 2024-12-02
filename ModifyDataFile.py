import numpy as np

filename = 'calcite1x1x1.lmp'

radius = 5.0

statusAtom = False
listMoltoDelete = []

atomic_info = np.loadtxt(filename,skiprows=18)
print(atomic_info)
exit()
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
    

        


# with open(filename, 'r') as file:
#     lines = file.readlines()

# print(lines)
# with open("new"+filename, 'w') as fp:
#     # iterate each line
#     for number, line in enumerate(lines):
#         # delete line 5 and 8. or pass any Nth line you want to remove
#         # note list index starts from 0
        
#         if len(splitted)>0:

            
#             if len(splitted)>1:
#                 if status == 'StatusAtoms' :
                        
                    

                
                
#             if splitted[0] == 'Atoms' :
#                 status = 'StatusAtoms'
            

#         fp.write(line)
              

# print(atom_to_delete)
# print(listMoltoDelete)

    
    