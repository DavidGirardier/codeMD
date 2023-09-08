from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt
inputfile = '20Asso5nsdt0_01'
trajectories = np.loadtxt(inputfile)
print(np.mean(trajectories[:,1]))
numberBins = 100
dx=0.001
minPos = min(trajectories[:,1])
maxPos = max(trajectories[:,1])
histo_pos = np.histogram(trajectories[:,1], np.arange(minPos,maxPos,dx))
F=[]
summm = 0.
for i in histo_pos[0]:
    summm +=i 
    if i!=0.0:
        F.append(-np.log(i/(len(trajectories[:,1]))))
    else:
        F.append(0.0)
#F = [-np.log(x) for x in histo_pos[0] if x>0]

np.savetxt('FEfromRho_' + inputfile, np.c_[histo_pos[1][:-1],F-min(F),histo_pos[0]/(len(trajectories[:,1]))], header='# x F rho')
exit()
print(minPos)
print(maxPos)
sizeBin = (maxPos - minPos)/numberBins
counter = 0
arrayBins = np.zeros((numberBins,2))
y = np.zeros(numberBins)
x = np.zeros(numberBins)

for k in range(np.size(arrayBins,0)):
    arrayBins[k][0] = k*sizeBin - minPos



for i in range(np.size(trajectories, 0)):
    counter += 1 
    #print(trajectories[i][1])
    associatedBin = int((trajectories[i][1] - minPos)/sizeBin)
    arrayBins[associatedBin][1] += 1

for k in range(np.size(arrayBins,0)):
    
    y[k] = arrayBins[k][1]/counter
    x[k] = arrayBins[k][0]
    #print(str(x[k])+'\t'+str(y[k]))



# plt.plot(x,y)
# plt.plot(x,-np.log(y))
# plt.show()

F=[]
for i in range(np.size(arrayBins,0)):
    if y[i]!=0.0:
        F.append(-np.log(y[i]))
    else:
        F.append(0.0)
        

# np.savetxt('FEfromRho', np.c_[x,-np.log(y),y], header='# x F rho')
np.savetxt('FEfromRho', np.c_[x,F], header='# x F rho')

x_final = [trajectories[i-1][1] for i in range(101,len(trajectories)+1, 101)]
#v_final = [trajectories[i-1][2] for i in range(101,len(trajectories)+1, 101)]
print(np.var(x_final))
#print(np.var(v_final))
#np.savetxt('FEFull', np.c_[x,y], header='# x rho')
