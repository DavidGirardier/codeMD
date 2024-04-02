import numpy as np
import random

inputfile = 'lastRunAccepted.txt'
lastRunAcc = np.loadtxt(inputfile)
allt = []
allq = []
count=0
i=0
start = int(len(lastRunAcc)/3)
#random.shuffle(lastRunAcc)

for i in lastRunAcc[start:]:
    count = count + 1
    if count>50:
        break
    fw = np.loadtxt('cv_'+str(int(i))+'_fw')
    bw = np.loadtxt('cv_'+str(int(i))+'_bw')
    allt.extend(fw[:,0])
    allt.extend(bw[:,0])
    allq.extend(fw[:,1])
    allq.extend(bw[:,1])


outputName=str(2*(count-1))+'colvar_c60_mO1'
np.savetxt(outputName, np.c_[allt, allq], fmt='%1.8E')
print(outputName)
#