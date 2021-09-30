from numpy import sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz

inputfile = input("Diff file: ")
file = open(inputfile, 'r')
Lines = file.readlines()
counter = -1
dt=[]
xx=[]
yy=[]
zz=[]
xy=[]
xz=[]
yx=[]
Nt=5000
for line in Lines:

    counter = counter + 1
    if (counter < Nt) :
        splitted = line.split()
        splitted = [float(i) for i in splitted] #split each line

        dt.append(splitted[0])
        xx.append(splitted[1])
        yy.append(splitted[2])
        zz.append(splitted[3])
        xy.append(splitted[4])
        xz.append(splitted[5])
        yx.append(splitted[6])

    if (counter==Nt):
        break
        counter = -1

dt = array(dt)
xx = array(xx)
yy = array(yy)
zz = array(zz)
xy = array(xy)
xz = array(xz)
yx = array(yx)


Dxx = []
Dyy = []
Dzz = []
Dxy = []
Dxz = []
Dyx = []
sum=0.0
Integral = []
for t in range(Nt):
    print(xx[t])
    Dxx.append(trapz(xx[:t+1],dt[:t+1]))
    Dyy.append(trapz(yy[:t+1],dt[:t+1]))
    Dzz.append(trapz(zz[:t+1],dt[:t+1]))
    Dxy.append(trapz(xy[:t+1],dt[:t+1]))
    Dxz.append(trapz(xz[:t+1],dt[:t+1]))
    Dyx.append(trapz(yx[:t+1],dt[:t+1]))
#     d=(xx[t+1]+xx[t])/2*dt[1]
#     sum=sum+d
#     print(d)
#     Integral.append(sum)
#
# Integral = array(Integral)
Dxx = array(Dxx)
Dyy = array(Dyy)
Dzz = array(Dzz)
Dxy = array(Dxy)
Dxz = array(Dxz)
Dyx = array(Dyx)
outputfile = 'diffusion_' + inputfile
savetxt(outputfile, c_[dt,Dxx,Dyy,Dzz,Dxy,Dxz,Dyx])
