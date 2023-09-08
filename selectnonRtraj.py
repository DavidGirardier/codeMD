import numpy as np
import random


allt = []
allq = []
count=0
i=0
nshooting = 500
arr = np.arange(1,nshooting+1)
np.random.shuffle(arr)

for i in arr:

    fw = np.loadtxt('colvar/cv_'+str(int(i))+'_fw')
    bw = np.loadtxt('colvar/cv_'+str(int(i))+'_fw')
    allt.extend(fw[:,0])
    allt.extend(bw[:,0])
    allq.extend(fw[:,1])
    allq.extend(bw[:,1])


outputName=str(int(2*nshooting)) + 'NonReactive_colvar_c60_precise'
np.savetxt(outputName, np.c_[allt, allq], fmt='%1.10E')
#