import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot(111, projection='3d')
x = 0.
y = 0.
z = 0.
#inputfile = "lowdensityEqT3.txt"
#inputfile = "lowdensityEqT.txt"
inputfile = "6part.txt"
#inputfile = "Shuffled_checkpoint.txt"
#inputfile = "checkpoint.txt"
#inputfile = "3part.txt"
#inputfile = "moreBigpart.txt"
# inputfile = "EXPLOSION.txt"
#inputfile = "explosionLJCellList.txt"
#inputfile = "trapped.txt"
file = open(inputfile, 'r')
Lines = file.readlines()
counter = -1
splitted = Lines[0].split()
splitted = [float(i) for i in splitted]
N = int(splitted[0])
boxLenght = splitted[1]
headerLine = str(N) + '\t' + str(boxLenght)
shufflingList = []

ax.set_proj_type('ortho')


for k in range(1,N+1):
    splitted = Lines[k].split()
    splitted = [float(i) for i in splitted]

    x = splitted[0] - boxLenght*round(splitted[0]/boxLenght)
    y = splitted[1] - boxLenght*round(splitted[1]/boxLenght)
    z = splitted[2] - boxLenght*round(splitted[2]/boxLenght)
    
    if (k<101):
        ax.scatter(x,y,z, c='red', s=1000, alpha=0.5)
    else :
        ax.scatter(x,y,z, c='blue', s=1000, alpha=0.5)


    # if (k==2) or (k==3):
    #     ax.scatter(x,y,z, c='black', s=1000, alpha=0.5)

    



 # plot the point (2,3,4) on the figure

plt.show()