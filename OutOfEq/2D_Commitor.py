import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pot import Z1,Z2

#rx=2.0, ry=0.5

@jit(nopython=True)
def is_in_region_A(x, y, xyA, rx=1.0, ry=1.0):
    return (x - xyA[0])**2 /rx**2 + (y - xyA[1])**2/ry**2 < 1
@jit(nopython=True)
def is_in_region_B(x, y, xyB,  rx=1.0, ry=1.0):
    return (x - xyB[0])**2 /rx**2 + (y - xyB[1])**2/ry**2 < 1

@jit(nopython=True)
def EulerMaruyamaComm(mass, gamma, kT, initialPosition, initialVelocity, timeStep, totalTime,Pot,xyA,xyB):

    
    x = initialPosition[0]
    y = initialPosition[1]

    vx = initialVelocity[0]
    vy = initialVelocity[1]
    
    for i in range(int(totalTime/timeStep)+1):

        
        Fx, Fy, _ = Pot(x,y)
        Fx = -Fx
        Fy = -Fy

        randomNumberx = np.random.normal()
        randomNumbery = np.random.normal()
        
        x_new = x + vx*timeStep
        sigma = np.sqrt(2.*kT*gamma/mass)
        vx_new = vx - gamma*vx*timeStep + timeStep*Fx/mass + np.sqrt(timeStep)*sigma*randomNumberx 
              
        y_new = y + vy*timeStep
        sigma = np.sqrt(2.*kT*gamma/mass)
        vy_new = vy - gamma*vy*timeStep + timeStep*Fy/mass + np.sqrt(timeStep)*sigma*randomNumbery
        
        x = x_new
        y = y_new
        vx = vx_new
        vy = vy_new

        if is_in_region_A(x, y, xyA):
            return 'A'
        if is_in_region_B(x, y, xyB):
            return 'B'
    return 'R'#, velocitiesx, velocitiesy

   
ntraj=1000
m = 1.
g = 50.
kT = 1.

dt=0.001
tot_t=1000


all_t = []
all_x = []
all_y = []

BassinA = (-1.,0.)
BassinB = (1.,0.)
# BassinA = (-2.,-1.)
# BassinB = (2.,1.)

# xrange = (-4,4)
# yrange = (-1.5,1.5)

xrange = (-4,4)
yrange = (-1.5,1.5)

npointsx = 100
npointsy = 100


x_values = np.linspace(xrange[0], xrange[1], npointsx)
y_values = np.linspace(yrange[0], yrange[1], npointsy)
initial_points = [(x, y) for x in x_values for y in y_values]


# for i, (x0, y0) in enumerate(initial_points):
#     if is_in_region_A(x0, y0, BassinA, rx=2.0, ry=0.5):
#         plt.plot(x0,y0,'.',color='red')
#     elif is_in_region_B(x0, y0, BassinB, rx=1.0, ry=1.0):
#         plt.plot(x0,y0,'.',color='black')
#     plt.xlim((-4,4))
#     plt.ylim((-4,4))
# plt.gca().set_aspect('equal', adjustable='box')
# plt.show()
# exit()
#     counterA = 0
#     for j in range(ntraj):
#         pos0 = [x0,y0]
#         which_bassin = EulerMaruyamaComm(m,g,kT,pos0,[0,0],dt,tot_t,Z2,BassinA,BassinB)
#         if which_bassin == 'A':
#             counterA = counterA +1
#     if counterA > 25 : plt.plot(x0,y0,'.')
# plt.show()
# print(initial_points)
# exit()
matrixCommitor = []

for i, (x0, y0) in enumerate(initial_points):
    print(i)
    counterA = 0
    counterB = 0
    pos0 = [x0,y0]
    for j in range(ntraj):
        vel0x = np.sqrt(kT/m) * np.random.normal()
        vel0y = np.sqrt(kT/m) * np.random.normal()
        which_bassin = EulerMaruyamaComm(m,g,kT,pos0,[vel0x,vel0y],dt,tot_t,Z1,BassinA,BassinB)
        if which_bassin == 'A':
            counterA = counterA +1
        
        if which_bassin == 'B':
            counterB = counterB +1
        
    commitor = counterA/(counterA+counterB)
    #print(commitor)
    matrixCommitor.append(commitor)
    

print(commitor)
print(counterA+counterB)
matrixCommitor = np.array(matrixCommitor)

#np.savetxt('commZ1', matrixCommitor, fmt='%1.8E')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#print(len(committor_values2))
comm = matrixCommitor.reshape(npointsx, npointsy) #order='F')
#print(comm)
# Plot
output_name = 'comm_Z1g'+str(g)+ 'ntraj'+str(ntraj)
head = str(xrange[0])+' '+str(xrange[1])+' '+str(yrange[0])+' '+str(yrange[1])+' '+str(npointsx)+' '+str(npointsy)
np.savetxt(output_name, comm, fmt='%1.8E',header=head)
X, Y = np.meshgrid(x_values, y_values)

plt.figure(figsize=(6, 5))
plt.imshow(comm, extent=[x_values.min(), x_values.max(), y_values.min(), y_values.max()],
           origin='lower', cmap='viridis', aspect='auto')

# Add a color bar to show the color scale
plt.colorbar(label='Comm Values')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("2D Colormap of Comm Data")

plt.show()    
    

# outputName='ntraj'+str(ntraj)+'_Z1g'+str(g)+ 'm' + str(m)

# np.savetxt(outputName, np.c_[all_t,all_x,all_y], fmt='%1.8E')





exit()
bins = 50

# Calculate the 2D histogram
hist, x_edges, y_edges = np.histogram2d(pos_x, pos_y, bins=bins, range=[[-1.5, 1.5], [-1.5, 1.5]])

# Normalize the histogram
bin_area = (x_edges[1] - x_edges[0]) * (y_edges[1] - y_edges[0])  # Area of each bin
hist_normalized = hist / (len(pos_x) * bin_area)  # Normalized to probability density

# Plot the normalized histogram
plt.imshow(hist_normalized.T, origin='lower', extent=[-1.5, 1.5, -1.5, 1.5], cmap='viridis', aspect='auto')

# Add a color bar
plt.colorbar(label='Probability Density')

# Label the axes
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Normalized 2D Histogram of Particle Positions')

# Show the plot
plt.show()