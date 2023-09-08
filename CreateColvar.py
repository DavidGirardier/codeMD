from numpy import savetxt, zeros, c_, arange
from random import random


from random import seed

seed(1)
startQ=0.0
t = []
pos = []
time = 10.0
numberofTraj = 100
dt = 0.01
for j in range(numberofTraj):
    for i in range(0, int(time/dt)+1):
        t.append(i*dt)
        if i == 0 or i == 1:
            x = startQ
        else:
            x = random()*0.15
        pos.append(x)
        


savetxt('colvar100', c_[t,pos], fmt='%1.8E')