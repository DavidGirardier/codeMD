from mayavi import mlab
import numpy as np



x = 0.
y = 0.
z = 0.
inputfile = "checkpoint.txt"
file = open(inputfile, 'r')
Lines = file.readlines()
counter = -1
splitted = Lines[0].split()
splitted = [float(i) for i in splitted]
N = int(splitted[0])
boxLenght = splitted[1]
headerLine = str(N) + '\t' + str(boxLenght)
shufflingList = []

for k in range(1,N+1):
    splitted = Lines[k].split()
    splitted = [float(i) for i in splitted]

    x = splitted[0] - boxLenght*round(splitted[0]/boxLenght)
    y = splitted[1] - boxLenght*round(splitted[1]/boxLenght)
    z = splitted[2] - boxLenght*round(splitted[2]/boxLenght)
    
    if (k<101):
        mlab.points3d(x,y,z,1000)
    else :
        mlab.points3d(x,y,z,1000)

mlab.show()


