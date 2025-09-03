import numpy as np
import matplotlib.pyplot as plt
from numba import jit
from pot import Z1,Z2
from integratorsULE import EulerMaruyama
import pickle
from pathCV import s
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error

def mass_function(x,e,a,b,c):
    d=-0.5
    mass_x = e*(x+d)**12+a*(x+d)**4+b*(x+d)**2+c
    return mass_x
    
ntraj=100
m = 1.
g = 1.
kT = 1.

dt=0.001
tot_t=0.001
ev=1

all_t = []
all_x = []
all_y = []

xrange = (-2,2)
yrange = (-0.2,0.2)

npointsx = 101
npointsy = 11


x_values = np.linspace(xrange[0], xrange[1], npointsx)
y_values = np.linspace(yrange[0], yrange[1], npointsy)
initial_points = [(x, y) for x in x_values for y in y_values]

x_ref_range = (-2,2)
npointsref = 21
lamb = 1./((x_ref_range[1]-x_ref_range[0])/(npointsref-1))
x_ref = np.linspace(x_ref_range[0], x_ref_range[1], npointsref)
y_ref = x_ref*0.
references = [np.array([x_ref[i],y_ref[i]]) for i in range(npointsref)]

# all_vel_s = np.zeros((npointsx,npointsy))
# for x_i in range(npointsx):
#     for y_i in range(npointsy):
#         array_vels = []
#         array_velq = []
#         pos0 = [x_i,y_i]
#         for traj_i in range(ntraj):
#             vel0x = np.sqrt(kT/m) * np.random.normal()
#             vel0y = np.sqrt(kT/m) * np.random.normal()
#             t, pos_x, pos_y = EulerMaruyama(m,g,kT,pos0,[vel0x,vel0y],dt,tot_t,Z1)
#             s0 = s(np.array([pos_x[0],pos_y[0]]),references,1)
#             s1 = s(np.array([pos_x[1],pos_y[1]]),references,1)
#             vels = (s1-s0)/dt
#             array_vels.append(vels)
        
#         array_vels=np.array(array_vels)

#         mass = 1./np.mean(array_vels*array_vels)
#         all_vel_s[x_i,y_i] = mass

    


# plt.figure(figsize=(6, 5))
# plt.imshow(np.transpose(all_vel_s), extent=[x_values.min(), x_values.max(), y_values.min(), y_values.max()],
#            origin='lower', cmap='viridis', aspect='auto')

# # Add a color bar to show the color scale
# plt.colorbar(label='s Values')

# plt.scatter(x_ref, y_ref, color='black', facecolors='none', marker='o', label='path')

# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("2D s(R) values")

# plt.show()   
# exit()
s0_array = []
mass_array = []
for (x0, y0) in initial_points:
    array_vels = []
    array_velq = []
    pos0 = [x0,y0]
    for traj_i in range(ntraj):
        vel0x = np.sqrt(kT/m) * np.random.normal()
        vel0y = np.sqrt(kT/m) * np.random.normal()
        t, pos_x, pos_y = EulerMaruyama(m,g,kT,pos0,[vel0x,vel0y],dt,tot_t,Z1)
        s0 = s(np.array([pos_x[0],pos_y[0]]),references,lamb)
        s1 = s(np.array([pos_x[1],pos_y[1]]),references,lamb)
        vels = (s1-s0)/dt
        q0=pos_x[0]
        q1=pos_x[-1]
        velq = (q1-q0)/dt
        array_vels.append(vels)
        array_velq.append(velq)
    array_vels=np.array(array_vels)
    array_velq=np.array(array_velq)
    mass = 1./np.mean(array_vels*array_vels)
    mass_array.append(mass)
    s0_array.append(s0)
    massq = 1./np.mean(array_velq*array_velq)
    # v2=np.mean(array_velcomm*array_velcomm)
    # if v2>0.001:
    #plt.plot(x0,massq, '.', color='black')
    plt.plot(s0,mass, '.', color='black')
    plt.xlabel('pathCV')
    plt.ylabel('s')
    
    #plt.ylim((0,10))
    #print('committor = '+ str(x0) + '\t mass = '+ str(mass))
mass_array=np.array(mass_array)
s0_array=np.array(s0_array)
print(mass_array*mass_array)
popt, _ = curve_fit(mass_function, s0_array, mass_array, p0=[1.0,1.0,1.0,1.0])

# Extract the fitted parameters
e,a,b,c = popt
#print(f"Fitted parameters: x0={x0}, k={k}")

# Compute the fitted values
y_fitted = mass_function(s0_array, *popt)

# Calculate the Mean Squared Error
mse = mean_squared_error(mass_array, y_fitted)

print(f"MSE: {mse}")
s_plot = np.linspace(0,1,100)
print(*popt)

plt.plot(s_plot, mass_function(s_plot,e,a,b,c), label="Fitted Mass", color="blue")

plt.show()
        
    