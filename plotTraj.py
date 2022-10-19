import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot(111, projection='3d', proj_type = 'ortho')
x = 0.
y = 0.
z = 0.
xyzsplitted = []
inputfile = 'Trajectory.xyz'
Time = 10**25
file = open(inputfile, 'r')
Lines = file.readlines()
counter = -1
for t in range(0,Time,1):
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    ax.set_zlim(-10,10)
    splitted = Lines[0].split()
    splitted = [float(i) for i in splitted]
    N = int(splitted[0])

    # for k in range(3+t*(N+2),t*(N+2)+(N+2)):
    for k in range(N-1):
        splitted = Lines[k+t*(N+2)+2].split()
        xyzsplitted = [float(i) for i in splitted[1:]]
        name = splitted[0]
        x = xyzsplitted[0] 
        y = xyzsplitted[1] 
        z = xyzsplitted[2]


        if (name=='Big') :
            ax.scatter(x,y,z, c='red', s=1000, alpha=0.7)
        
        if (name=='Small'):
            ax.scatter(x,y,z, c='blue', s=1000, alpha=0.7)


        # if (k==2) or (k==3):
        #     ax.scatter(x,y,z, c='black', s=1000, alpha=0.5)
    plt.pause(0.01)
    plt.cla()
      



    # plot the point (2,3,4) on the figure

plt.show()