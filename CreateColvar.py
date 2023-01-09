from numpy import savetxt, zeros, c_, arange
from random import random


from random import seed

seed(1)

t = []
pos = []
for j in range(500):
    for i in range(0, 1000+1):
        t.append(i/1000.)
        if i == 0 or i == 1:
            x = 0
        else:
            x = random()*0.15
        pos.append(x)
        


savetxt('colvar100', c_[t,pos], fmt='%1.8E')