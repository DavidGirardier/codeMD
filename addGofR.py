import numpy as np

inputfile1 = "1_20607/merged_GofR.txt"
inputfile2 = "rdf/added2345_GofR.txt"
outputfile = open("added_GofR.txt", 'w')
angtoau_factor = 1.8897261254535
scaling = angtoau_factor
column = 1

#veltoau_factor = 1.8897261254535/(4.1341373336493*(10**3))


file = open(inputfile1, 'r')
Lines = file.readlines()
count = 0

arr1=[]

for line in Lines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    arr1.append(splitted[:])

file = open(inputfile2, 'r')
Lines = file.readlines()

arr2=[]

for line in Lines:
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    arr2.append(splitted[:])



for i in range(count):
    outputfile.write(str(arr1[i][0]) + '\t' + str((arr1[i][1]*2. + arr2[i][1]*8.)/10.)+ '\t' + str((arr1[i][2]*2. + arr2[i][2]*8.)/10.) + '\t' + str((arr1[i][3]*2. + arr2[i][3]*8.)/10.) +'\n')



outputfile.close()
