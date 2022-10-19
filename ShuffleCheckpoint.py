import numpy as np
inputfile = "checkpoint.txt"
file = open(inputfile, 'r')
Lines = file.readlines()
counter = -1
splitted = Lines[0].split()
splitted = [float(i) for i in splitted]
N = int(splitted[0])
boxLenght = splitted[1]
headerLine = str(N) + '\t' + str(boxLenght)
shufflingList = []

for k in range(1,N+1):
    splitted = Lines[k].split()
    splitted = [float(i) for i in splitted]
    shufflingList.append(splitted) 

for i in range(100000*N):
    print(i)
    rand_num = np.random.uniform(0,1)
    randomNumber1 = int(N*rand_num)

    rand_num = np.random.uniform(0,1)
    randomNumber2 = int(N*rand_num)

    if randomNumber1 != randomNumber2:

        temporaryLine1 = shufflingList[randomNumber1]
        temporaryLine2 = shufflingList[randomNumber2]

        shufflingList[randomNumber1] = temporaryLine2
        shufflingList[randomNumber2] = temporaryLine1
outputName = 'Shuffled_' + inputfile
np.savetxt(outputName, shufflingList, header=headerLine, comments='')
