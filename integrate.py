from numpy import sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz

file = open('nomean_Na.out', 'r')
Lines = file.readlines()
counter = -1
dt=[]
xx=[]
yy=[]
zz=[]
xy=[]
for line in Lines:

    counter = counter + 1
    if (counter < 1000) :
        splitted = line.split()
        splitted = [float(i) for i in splitted] #split each line

        dt.append(splitted[0])
        xx.append(splitted[1])
        yy.append(splitted[2])
        zz.append(splitted[3])
        xy.append(splitted[4])
    if (counter==1000):
        break
        counter = -1

dt = array(dt)
xx = array(xx)
yy = array(yy)
zz = array(zz)
xy = array(xy)


Dxx = []
Dyy = []
Dzz = []
Dxy = []
for t in range(1000):
    Dxx.append(trapz(xx[:t+1],dt[:t+1]))
    Dyy.append(trapz(yy[:t+1],dt[:t+1]))
    Dzz.append(trapz(zz[:t+1],dt[:t+1]))
    Dxy.append(trapz(xy[:t+1],dt[:t+1]))

Dxx = array(Dxx)
Dyy = array(Dyy)
Dzz = array(Dzz)
Dxy = array(Dxy)


savetxt('diffusionnommean_Na.out', c_[Dxx,Dyy,Dzz,Dxy])
