import numpy as np


inputfile = 'multipleTrajdt0_01_long.txt'
trajectory = np.loadtxt(inputfile, max_rows=1000000)


numberOfFile = 100
tFile = 10000.0
t = numberOfFile*tFile
dt = 0.01
nLine = int(tFile/dt)
countTransition = 0
oldpos = ''
pos = ''
for j in range(numberOfFile+1):
    
    if j !=0:
       trajectory = np.loadtxt(inputfile, skiprows=nLine*j+1, max_rows=nLine) 
    for i in range(0,len(trajectory[:,0])):
        print(i)
        if trajectory[i,1] <= -0.75:
            pos = 'A'
        elif 0.75 <= trajectory[i,1]:
            pos = 'B'
        
        if oldpos != pos and pos !='' and oldpos !='':
            countTransition = countTransition + 1
        
        oldpos = pos
    print('Traj ' + str(j) + '\t done')
    oldpos = ''
    pos = ''
    trajectory = []

print('Number of Transtition = ' + str(countTransition))
print('MFPT = ' + str(t/countTransition))

