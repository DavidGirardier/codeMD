import numpy as np

oldfile = open('DissipationFunction_rs.txt', 'r')
newfile = open('data.inpt', 'w')

angtoau_factor = 1.8897261254535
veltoau_factor = 1.8897261254535/(4.1341373336493*(10**3))
Lines = oldfile.readlines()
arr = []
count = -1

for line in Lines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    if count%2 == 0:
        newfile.write('Na \t' + str(splitted[0]*angtoau_factor) +'\t'+ str(splitted[1]*angtoau_factor) +'\t'+ str(splitted[2]*angtoau_factor) + '\n')

for line in Lines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    if count%2 == 1:
        newfile.write('Cl \t' + str(splitted[0]*angtoau_factor) +'\t'+ str(splitted[1]*angtoau_factor) +'\t'+ str(splitted[2]*angtoau_factor) + '\n')

newfile.write('#velocities \n')

for line in Lines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    if count%2 == 0:
        newfile.write('Na \t' + str(splitted[3]*veltoau_factor) +'\t'+ str(splitted[4]*veltoau_factor) +'\t'+ str(splitted[5]*veltoau_factor) + '\n')

for line in Lines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    if count%2 == 1:
        newfile.write('Cl \t' + str(splitted[3]*veltoau_factor) +'\t'+ str(splitted[4]*veltoau_factor) +'\t'+ str(splitted[5]*veltoau_factor) + '\n')




newfile.close()
