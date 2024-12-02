import numpy as np


tableA = []
tableB = []

countA = 0
countB = 0

ntosel = 25
wholetraj=np.empty(0)
wholetime=np.empty(0)
for i in range(1,201):
    inputfile = 'cv_every250_'+str(i)
    trajectories = np.loadtxt(inputfile)
    print(i)
    
    for j in range(len(trajectories[:,1])):
        x = trajectories[j,1]
        if x < 2.75 and countA<ntosel:
            countA = countA + 1
            tableA.append(i)
            wholetime = np.concatenate((wholetime,trajectories[:j+10000,0]))
            wholetraj = np.concatenate((wholetraj,trajectories[:j+10000,1]))
            print('A')
            break
        if x > 3.3 and countB<ntosel:
            countB = countB + 1
            tableB.append(i)
            wholetime = np.concatenate((wholetime,trajectories[:j,0]))
            wholetraj = np.concatenate((wholetraj,trajectories[:j,1]))
            print('B')
            break
    print(wholetime)
    if (countA == ntosel) and (countB == ntosel):
        break
    print(tableA)
    print(len(tableA))
    print(tableB)        
    print(len(tableB))
            

print(tableA)
print(tableB)





outputName= "50shoot_newdt0.5"
# print(outputName)

np.savetxt(outputName, np.c_[wholetime,wholetraj], fmt='%1.8E')
# print([max(alltraj),min(alltraj)])
# np.savetxt(outputName+ 'qMinandMax', [max(alltraj),min(alltraj)], fmt='%1.8E')
