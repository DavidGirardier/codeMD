import numpy as np


tFile = 20.0
dt = 0.001
numberOfLine = int(tFile/dt)

inputfile1 = 'COLVAR'
inputfile2 = '.xyz'

numberOfAtoms = 120

massQ = []

for i in range(numberOfLine+1):
    mass = 0
    
    cv = np.loadtxt(inputfile1, skiprows=i, max_rows=1) 
    positionC60A = np.loadtxt(inputfile2, skiprows=(numberOfAtoms/2.)*i, max_rows=numberOfAtoms-1)
    positionC60B = np.loadtxt(inputfile2, skiprows=(numberOfAtoms/2.)*i+1, max_rows=numberOfAtoms-1)
    
    exit()
    for j in range(numberOfAtoms):
        derivative = 1./cv[1] * (np.mean(positionC60A[:][0]-np.mean(positionC60B[:][0]))) / 60.0


    
    



    

v2 = []
for i in range(np.size(positionAndvelocities,0)):
    v2.append(positionAndvelocities[i][1]*positionAndvelocities[i][1]) 
#print(1./(np.mean(v2)))
print(1./np.mean(v2))

 
numberBins = 10
minPos = 0.8
maxPos = 2.0
sizeBin = (maxPos - minPos)/numberBins
counter = 0
arrayBins = np.zeros((numberBins,2))
counterByBins = np.zeros(numberBins)

mass = np.zeros((numberBins,2))


for k in range(np.size(arrayBins,0)):
    arrayBins[k][0] = k*sizeBin + minPos
    mass[k][0] = k*sizeBin + minPos



for i in range(np.size(positionAndvelocities,0)):
    counter += 1 
    #print(i)
    associatedBin = int((positionAndvelocities[i][0] - minPos)/sizeBin)
    #print(positionAndvelocities[i][0])
    #print(positionAndvelocities[i][1])
    #print(associatedBin)
    arrayBins[associatedBin][1] += positionAndvelocities[i][1]*positionAndvelocities[i][1]
    #print(arrayBins)
    counterByBins[associatedBin] += 1.0
    #print(counterByBins)

   


for i in range(np.size(arrayBins,0)):
    
    if counterByBins[i] !=0:
        mass[i][1] = counterByBins[i]/arrayBins[i][1]

print(mass)
outputName = 'massq.txt'
np.savetxt(outputName, np.c_[mass], fmt='%1.4E')   
        

