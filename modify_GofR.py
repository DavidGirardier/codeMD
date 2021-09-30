import numpy as np

inputfile3 = "GofR_ClCl.txt"
inputfile1 = "GofR_ClNa.txt"
inputfile2 = "GofR_NaNa.txt"
outputfile = open("merged_GofR.txt", 'w')
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

file = open(inputfile3, 'r')
Lines = file.readlines()

arr3=[]

for line in Lines:
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    arr3.append(splitted[:])

for i in range(count):
    outputfile.write(str(arr1[i][0]*scaling) +'\t'+ str(arr1[i][1]) +'\t'+ str(arr2[i][1]) +'\t'+ str(arr3[i][1]) +'\n')



outputfile.close()
