import numpy as np


inputfile = 'cv'
trajectory = np.loadtxt(inputfile)
#trajectory = np.loadtxt(inputfile, max_rows=1000000)


numberOfFile = 1
#tFile = 500000.0
#t = numberOfFile*tFile
dt = 1.0
#nLine = int(tFile/dt)
countTransition = 0
oldpos = ''
pos = ''
time = 0.0
timeList = []
for j in range(numberOfFile):
    
    # if j !=0:
    #    trajectory = np.loadtxt(inputfile, skiprows=nLine*j+1, max_rows=nLine)

    for i in range(0,len(trajectory[:,0])):
        #print(i)
        time = time + dt
        
        if trajectory[i,1] <= 1.1:
            pos = 'A'
        elif 1.325 <= trajectory[i,1]:
            pos = 'B'
        
        if oldpos != pos and pos == 'B' and oldpos == 'A':
            timeList.append(time)
            countTransition = countTransition + 1

        if oldpos != pos and pos == 'A' and oldpos == 'B':
            time = 0.0
        
        oldpos = pos
    print('Traj ' + str(j) + '\t done')
    oldpos = ''
    pos = ''
    trajectory = []
print(timeList)
print('MFPT = ' + str(np.mean(timeList)) + ' +/- ' + str(np.sqrt(np.var(timeList) / len(timeList))) + ' ps')

with open('MFPT'+'_'+inputfile, 'a') as the_file:
    the_file.write('MFPT = ' + str(np.mean(timeList)) + ' +/- ' + str(np.sqrt(np.var(timeList) / len(timeList))) + ' ps')


