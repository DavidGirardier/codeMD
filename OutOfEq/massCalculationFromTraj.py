import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pot import Z1,Z2,Z3
from integratorsULE import EulerMaruyama
import pickle

def cond_avg_on_grid(x, om, *, edges=None, nbins=100):

    grid_edges = np.linspace(np.min(x), np.max(x), nbins + 1)
    
    # Compute bin centers from grid edges
    bin_centers = 0.5 * (grid_edges[:-1] + grid_edges[1:])
    
    # Assign each position to a bin (np.digitize returns 1-indexed bins; subtract 1 for 0-indexing)
    bin_indices = np.digitize(x, grid_edges) - 1
    # print(grid_edges)
    # print(x[0:500])
    # print(bin_indices[0:500])
    # exit()
    # Initialize an array to store the mean of velocities squared in each bin.
    
    mean_om = np.empty(nbins)
    mean_om.fill(np.nan)
    var_om = np.empty(nbins)
    var_om.fill(np.nan)

    # Loop over each bin and compute the mean of squared velocities.
    for i in range(nbins):
        # Select velocities corresponding to the current bin.
        bin_om = om[bin_indices == i]

        if bin_om.size > 0:
            # Compute the mean of the squared velocities.
            mean_om[i] = np.mean(bin_om)
            var_om[i] = np.var(bin_om)

    return bin_centers, mean_om
def cv(x,y):
    value_cv = 2.*(np.array(x)+4.)**(0.5) #+ 2.*(np.array(y)+4.)**(0.5) #(np.array(x)+2.)**(-1)
    return value_cv

def delta_approx(x, eps=1e-3):
    return np.exp(-x**2 / (2 * eps**2)) / (np.sqrt(2 * np.pi) * eps)

def compute_full_mass(m_int,cv,potential,q):
    xrange = (-2,2)
    yrange = (-2,2)

    npointsx = 101
    npointsy = 101


    x_values = np.linspace(xrange[0], xrange[1], npointsx)
    y_values = np.linspace(yrange[0], yrange[1], npointsy)
    num = 0.
    denom = 0.
    for i in range(len(x_values)-1):
        for j in range(len(y_values)-1):
            dqoverdrx = (cv(x_values[i+1],y_values[j])-cv(x_values[i],y_values[j]))/(x_values[i+1] - x_values[i])
            dqoverdry = (cv(x_values[i],y_values[j+1])-cv(x_values[i],y_values[j]))/(y_values[j+1] - y_values[j])
            overm_instant = (1./m_int*(dqoverdrx**2 + dqoverdry**2))

            num = num + overm_instant*potential(x_values[i],y_values[j])*delta_approx(cv(x_values[i],y_values[j])-q)
            denom = potential(x_values[i],y_values[j])*delta_approx(cv(x_values[i],y_values[j])-q)

    mq = num/denom
    return mq


ntraj=1
m_integration = 1.
g = 1.
kT = 1.

dt=0.001
tot_t=10000
ev=1

all_t = []
all_x = []
all_y = []

# xrange = (-2,2)
# yrange = (-0.2,0.2)

# npointsx = 101
# npointsy = 11


# x_values = np.linspace(xrange[0], xrange[1], npointsx)
# y_values = np.linspace(yrange[0], yrange[1], npointsy)
# initial_points = [(x, y) for x in x_values for y in y_values]

# x_ref_range = (-2,2)
# npointsref = 21
# lamb = 1./((x_ref_range[1]-x_ref_range[0])/(npointsref-1))
# x_ref = np.linspace(x_ref_range[0], x_ref_range[1], npointsref)
# y_ref = x_ref*0.
# references = [np.array([x_ref[i],y_ref[i]]) for i in range(npointsref)]

pos0 = [1,0]
all_overm = []
all_cv = []
all_v = np.empty(0)
for traj_i in range(ntraj):
    vel0x = np.sqrt(kT/m_integration) * np.random.normal()
    vel0y = np.sqrt(kT/m_integration) * np.random.normal()
    t, pos_x, pos_y = EulerMaruyama(m_integration,g,kT,pos0,[vel0x,vel0y],dt,tot_t,Z3)
    for j in range(len(t)-1):

        dqoverdrx = (cv(pos_x[j+1],pos_y[j])-cv(pos_x[j],pos_y[j]))/(pos_x[j+1] - pos_x[j])
        dqoverdry = (cv(pos_x[j],pos_y[j+1])-cv(pos_x[j],pos_y[j]))/(pos_y[j+1] - pos_y[j])
        overm_instant = (1./m_integration*(dqoverdrx**2 + dqoverdry**2))
        #print(overm_instant)
        all_cv.append(cv(pos_x[j],pos_y[j]))
        all_overm.append(overm_instant)
    plt.plot(t,cv(pos_x, pos_y))

    v = (np.array(cv(pos_x,pos_y)[1:]) - np.array(cv(pos_x,pos_y)[:-1]))/dt
    all_v = np.concatenate((all_v,v),axis=None)

print(1./np.mean(v*v))
plt.show()
# print(all_m)

print(1./np.mean(all_overm))

analytical_m = lambda q : (q**2)/4

centers, mean_overm = cond_avg_on_grid(np.array(all_cv), np.array(all_overm), nbins=10)
plt.figure(figsize=(8, 4))
plt.plot(centers, 1./mean_overm, 'o', markersize=4, label = 'numerical derivative')




print(len(all_cv))
print(len(all_v*all_v))

all_cv = np.array(all_cv)
#centers, mean_overm = cond_avg_on_grid(np.array(all_cv), np.array(all_overm), nbins=1)
centers, mean_overm = cond_avg_on_grid(all_cv, all_v*all_v, nbins=10)


plt.plot(centers,1./mean_overm, 'o', markersize=4, label = 'equipartition')
plt.plot(centers, analytical_m(centers), label = 'analytical')
plt.xlabel("Position (bin center)")
plt.ylabel("Mean mass")
plt.title("Conditional average of mass vs position")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.savefig("conditional_averageErgo.png", dpi=150)
plt.show()