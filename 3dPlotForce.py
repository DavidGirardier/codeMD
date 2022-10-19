import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
inputfile= os.path.join(dir_path,"../Multimaze", "plotForce1.txt")
#inputfile = 'plotForce1.txt'
file = open(inputfile, 'r')
Lines = file.readlines()
counter = -1
x = []
y = []
z = []
mapz = []
mapx = []
boxLenght = 79.490287059643592
x, y, z = np.loadtxt(inputfile,  usecols=(0, 1, 3), unpack=True)


"""mapz = np.reshape(z,(2000,2000))
# for i in range(800):
#     for j in range(800):
#         mapz[i][j] = np.log(mapz[i][j])
mapy = y[0:2000]
mapx = x[0::2000]
print(mapx)
"""



fig, ax = plt.subplots(subplot_kw={"projection": "3d"})   
surf = ax.plot_trisurf(x,y,z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# ax.set_zlim(-10**(-6), 10**(-6))
# ax.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
# ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
# ax.zaxis.set_major_formatter('{x:.02f}')

# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()

# fig = plt.figure(figsize =(14, 9))
# ax = plt.axes(projection ='3d')
 

# ax.plot_surface(x, y, z)

# plt.show()