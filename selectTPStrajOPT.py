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
alltraj=np.empty((0,9))
for i in lastRunAcc[start:]:
    print(i)
    count = count + 1
    if count>50:
        break
    fw = np.loadtxt('fw_'+str(int(i)),comments=['#', '$', '@'])
    bw = np.loadtxt('bw_'+str(int(i)),comments=['#', '$', '@'])
    e_fw = np.loadtxt('e_fw_'+str(int(i))+'.xvg',comments=['#', '$', '@'])
    e_bw = np.loadtxt('e_bw_'+str(int(i))+'.xvg',comments=['#', '$', '@'])
    allt.extend(fw[:,0])
    allt.extend(bw[:,0])
    fw = np.concatenate((fw,e_fw[:,1:3]),axis=1)
    bw = np.concatenate((bw,e_bw[:,1:3]),axis=1)
    alltraj = np.concatenate((alltraj,fw),axis=0)
    alltraj = np.concatenate((alltraj,bw),axis=0)
    

outputName=str(2*(count-1))+'colvar_c60_opt'
np.savetxt(outputName, alltraj, fmt='%1.8E')
print(outputName)
#