import numpy as np



name = 'LogLUDevGD'
matrix = np.loadtxt(name)

minbyG = []

friction = []

correction = []

for j in range(20):
    
    minNow = 0.
    frictionNow = 0.
    correctionNow = 0.
    
    for i in range(200):
        print(matrix[i*j+i,2])
        if sum(matrix[i*j+i,2:6])<=minNow:
            print('enter')
            minNow = sum(matrix[i*j+i,2:6])
            frictionNow = matrix[i*j+i,0]
            correctionNow = matrix[i*j+i,1]
    print(frictionNow)
    exit()
    
    minbyG.append(maxNow)
    friction.append(frictionNow)
    correction.append(correctionNow)
print(correction)
exit()
outputName='MinLogLbyLine'
np.savetxt(outputName, np.c_[friction, correction, maxbyG], fmt='%1.8E')  