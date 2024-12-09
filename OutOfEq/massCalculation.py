import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pot import Z1,Z2
from integratorsULE import EulerMaruyama
import pickle

with open('spline.pkl', 'rb') as f:
    loaded_spline = pickle.load(f)
    
ntraj=1000
m = 1.
g = 1.
kT = 1.

dt=0.001
tot_t=0.001
ev=1

all_t = []
all_x = []
all_y = []


xrange = (-0.5,0.5)
yrange = (0,0)

npointsx = 10000
npointsy = 1


x_values = np.linspace(xrange[0], xrange[1], npointsx)
y_values = np.linspace(yrange[0], yrange[1], npointsy)
initial_points = [(x, y) for x in x_values for y in y_values]



for i, (x0, y0) in enumerate(initial_points):
    array_velcomm = []
    array_velq = []
    pos0 = [x0,y0]
    for j in range(ntraj):
        vel0x = np.sqrt(kT/m) * np.random.normal()
        vel0y = np.sqrt(kT/m) * np.random.normal()
        t, pos_x, pos_y = EulerMaruyama(m,g,kT,pos0,[vel0x,vel0y],dt,tot_t,Z1)
        comm0 = loaded_spline(pos_x[0],pos_y[0])
        comm1 = loaded_spline(pos_x[-1],pos_y[-1])
        velcomm = (comm1-comm0)/dt
        q0=pos_x[0]
        q1=pos_x[-1]
        velq = (q1-q0)/dt
        array_velcomm.append(velcomm)
        array_velq.append(velq)
    array_velcomm=np.array(array_velcomm)
    array_velq=np.array(array_velq)
    mass = 1./np.mean(array_velcomm*array_velcomm)
    massq = 1./np.mean(array_velq*array_velq)
    # v2=np.mean(array_velcomm*array_velcomm)
    # if v2>0.001:
    #plt.plot(x0,massq, '.', color='black')
    plt.plot(comm0,mass, '.', color='black')
    plt.xlabel('committor')
    plt.ylabel('mass')
    
    plt.ylim((0,0.5))
    #print('committor = '+ str(x0) + '\t mass = '+ str(mass))
plt.show()
        
    