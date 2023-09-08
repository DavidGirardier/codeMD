import numpy as np
import random

inputfile = 'lastRunAccepted.txt'
lastRunAcc = np.loadtxt(inputfile)
allt = []
allq = []
count=0
i=0

random.shuffle(lastRunAcc)

for i in lastRunAcc:
    count = count + 1
    if count>250:
        break
    fw = np.loadtxt('colvar/cv_'+str(int(i))+'_fw')
    bw = np.loadtxt('colvar/cv_'+str(int(i))+'_fw')
    allt.extend(fw[:,0])
    allt.extend(bw[:,0])
    allq.extend(fw[:,1])
    allq.extend(bw[:,1])


outputName='500colvar_c60_precise'
np.savetxt(outputName, np.c_[allt, allq], fmt='%1.8E')
#