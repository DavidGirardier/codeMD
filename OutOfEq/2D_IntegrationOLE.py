import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pot import Z1,Z2,Z3,DW10
from integratorsOLE import EulerMaruyamaOLE


    
ntraj=100
m = 1.
D = [1.,1.]
kT = 1.
pos0 = [0.,0.]
dt=0.0001
tot_t=0.2
ev=1

all_t = []
all_x = []
all_y = []

for i in range(ntraj):
    vel0x = np.sqrt(kT/m) * np.random.normal()
    vel0y = np.sqrt(kT/m) * np.random.normal()
    t, pos_x, pos_y, d_x, d_y = EulerMaruyamaOLE(m,D,kT,pos0,dt,tot_t,DW10)
    
    outputName='OLEntraj'+str(ntraj)+'_DW10D'+str(D[0])+ 'm' + str(m) +'dt_'+ str(dt*ev)+ '_'+str(i)

    np.savetxt(outputName, np.c_[t[::ev],pos_x[::ev],pos_y[::ev]], fmt='%1.8E')
    np.savetxt('x'+outputName, np.c_[t[::ev],pos_x[::ev]], fmt='%1.8E')
    np.savetxt('y'+outputName, np.c_[t[::ev],pos_y[::ev]], fmt='%1.8E')
    q = (np.array(pos_x[::ev]) + np.array(pos_y[::ev]))/2
    np.savetxt('q'+outputName, np.c_[t[::ev],q], fmt='%1.8E')
    # all_t = all_t + t
    # all_x = all_x + pos_x
    # all_y = all_y + pos_y
    print('Dx = ', 0.5*np.var(d_x)/dt)
    print('Dy = ', 0.5*np.var(d_y)/dt)
    q = (np.array(d_x)+np.array(d_y))/2.
    print('Dq = ', 0.5*np.var(q)/dt)


    plt.plot(pos_x,pos_y)
    print('traj : '+str(i)+'/'+str(ntraj))

# outputName='ntraj'+str(ntraj)+'_Z1g'+str(g)+ 'm' + str(m)

# np.savetxt(outputName, np.c_[all_t,all_x,all_y], fmt='%1.8E')

plt.show()



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