from pot import Z1,Z2
import numpy as np
import matplotlib.pyplot as plt
from numba import jit

xrange = (-5,5)
yrange = (-2,2)

npointsx = 1000
npointsy = 1000


x_values = np.linspace(xrange[0], xrange[1], npointsx)
y_values = np.linspace(yrange[0], yrange[1], npointsy)
initial_points = [(x, y) for x in x_values for y in y_values]


matrixPot = []

for i in x_values:
    for j in y_values:
        fx,fy,e =Z2(i,j)
        matrixPot.append(e)

matrixPot = np.array(matrixPot)


desired_max=100
#print(len(committor_values2))
Pot = matrixPot.reshape(npointsx, npointsy) #order='F')
im = plt.imshow(np.transpose(Pot), 
                extent=[x_values.min(), x_values.max(), y_values.min(), y_values.max()],
                origin='lower', cmap='viridis', aspect='auto', 
                vmax=desired_max)

# Add contour lines automatically
contour_levels=np.arange(1,100,10)
contour = plt.contour(x_values, y_values, Pot.T, levels=contour_levels,colors='black', linewidths=0.5)

# Add a color bar to show the color scale
plt.colorbar(im, label='kT')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Z2 potential")

plt.show()