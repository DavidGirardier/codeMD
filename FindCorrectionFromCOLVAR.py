import numpy as np

numberOfFile = 500
tFile = 1000.
dt = 0.01
kTovermass= 1./120.
nLine = int(tFile/dt +1)

inputfile = input('inpute file:')
positionAndvelocities = []
meanv2=0.
counterTraj = 0
allMean = 0.0
allMeanList = []
allTime = []
for j in range(numberOfFile):
    
    counter = 0
    meanv2 = 0.0
    trajectory = np.loadtxt(inputfile, skiprows=nLine*j, max_rows=nLine) 
    
    for k in range(1,len(trajectory)-1):
        
        velocity = (trajectory[k+1][1]-trajectory[k-1][1])/(2.*dt)
        #print(velocity)
        #velocity = (trajectory[k+1][1]-trajectory[k][1])/(dt)
        counter = counter + 1
        meanv2 = meanv2 + velocity*velocity
    
    counterTraj = counterTraj + 1
    allMean = allMean + meanv2/counter
    allMeanList.append(allMean/counterTraj)
    allTime.append(counter*dt*counterTraj)
    print(1./(allMean/counterTraj))
    #print('Traj' + str(j)+ ' Done')
    trajectory = []
#print(positionAndvelocities)






outputName = 'meanU2COLVAR.txt'
np.savetxt(outputName, np.c_[allTime, allMeanList], fmt='%1.8E')
exit()

numberBins = 40
minPos = -1.8
maxPos = 1.8
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
        

