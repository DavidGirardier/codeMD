import numpy as np

numberOfFile = 5
tFile = 2000.
dt = 0.001

nLine = int(tFile/dt +1)

inputfile = input('inpute file:')
positionAndvelocities = []

fromPosorVel = 'q'
maxQ=-1000.
minQ=1000.
everyList = np.arange(1,10,1)
matrixMass=[]
mass = []
error = []

if fromPosorVel == 'q':
    for j in range(numberOfFile):
        mass = []
        trajectory = np.loadtxt(inputfile, skiprows=nLine*j, max_rows=nLine) 
        print(trajectory)
        for every in everyList:
        
        
            for k in range(1+every,len(trajectory)-1*every,every):
                
                velocity = (trajectory[k+1*every][1]-trajectory[k-1*every][1])/(2.*dt*every)
                
                #print(velocity)
                #velocity = (trajectory[k+1][1]-trajectory[k][1])/(dt)
                positionAndvelocities.append([trajectory[k][1], velocity])
            #print('traj' + str(j) + 'done')

            if max(trajectory[:,1])>maxQ:
                maxQ=max(trajectory[:,1])

            if min(trajectory[:,1])<minQ:
                minQ=min(trajectory[:,1])

    # print('Position max = ' + str(maxQ))
    # print('Position min = ' + str(minQ))


    # if fromPosorVel == 'v':
    #     for j in range(numberOfFile):
            
            
    #         trajectory = np.loadtxt(inputfile, skiprows=nLine*j, max_rows=nLine) 
            
            
    #         for k in range(0,len(trajectory)):
    #             positionAndvelocities.append([trajectory[k][1], trajectory[k][2]])
    #         #print('traj' + str(j) + 'done')

            v = []
            v2 = []
            myMean=0.0
            for i in range(np.size(positionAndvelocities,0)):
                
                v.append(abs(positionAndvelocities[i][1])) 
                v2.append(positionAndvelocities[i][1]*positionAndvelocities[i][1]) 
                # myMean += positionAndvelocities[i][1]*positionAndvelocities[i][1]
                # if i%10000==0:
                #     print(myMean/i)

            #print(np.mean(v2))
            #print('mass =' + str(1./np.mean(v2)))
            mass.append(1./np.mean(v2))
            #error.append((2./np.mean(v)**3)*np.sqrt(np.var(v2))/np.sqrt(len(v2)))
            positionAndvelocities = []
            v2=[]
        matrixMass.append(mass)
print(matrixMass)
mean_curve = np.mean(matrixMass, axis=0)

# Compute the variance of the aligned curves
variance_curve = np.var(matrixMass, axis=0)/np.sqrt(numberOfFile)
outputName = 'mass_'+ inputfile
np.savetxt(outputName, np.c_[everyList,mean_curve,variance_curve], fmt='%1.6E')

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
        

