import numpy as np
from scipy.interpolate import SmoothBivariateSpline, RectBivariateSpline,interp2d
import matplotlib.pyplot as plt
import glob
import pickle
from pot import Z1,Z2
from numba import jit

@jit(nopython=True)
def s(R,ref,l):
    P = len(ref)
    num=0.
    denom=0.
    for r in range(P):
        #print(np.linalg.norm(R-ref[i]))
        num = num + (r)*np.exp(-l*(np.linalg.norm(R-ref[r])))
        denom = denom + np.exp(-l*(np.linalg.norm(R-ref[r])))
    if denom != 0:    
        s_cv = num/denom/(P-1) 
        #exit()
        #print(s_cv)   
        return s_cv
    else:
        return 2.


# xrange = (-2,2)
# yrange = (-1,1)

# npointsx = 1000
# npointsy = 10


# x_values = np.linspace(xrange[0], xrange[1], npointsx)
# y_values = np.linspace(yrange[0], yrange[1], npointsy)
# initial_points = [(x, y) for x in x_values for y in y_values]

# x_ref_range = (-1.,1.)
# npointsref = 11

# x_ref = np.linspace(x_ref_range[0], x_ref_range[1], npointsref)
# #y_ref = np.zeros(npointsref)
# y_ref = x_ref*0.
# #y_ref = x_ref*x_ref*x_ref

# references = [np.array([x_ref[i],y_ref[i]]) for i in range(npointsref)]

# # print(s(np.array([-3,0]),references,100))
# # exit()
# all_s = np.zeros((npointsx,npointsy))
# for x_i in range(npointsx):
#     for y_i in range(npointsy):
#         all_s[x_i,y_i]= s(np.array([x_values[x_i],y_values[y_i]]),references,4.6)
    


# plt.figure(figsize=(6, 5))
# plt.imshow(np.transpose(all_s), extent=[x_values.min(), x_values.max(), y_values.min(), y_values.max()],
#            origin='lower', cmap='viridis', aspect='auto')

# # Add a color bar to show the color scale
# plt.colorbar(label='s Values')

# plt.scatter(x_ref, y_ref, color='black', facecolors='none', marker='o', label='path')

# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("2D s(R) values")

# plt.show()
# for u in range(len(x_values)): 
#     plt.plot(x_values[u],s(np.array([x_values[u],0.]),references,4.6),'.')
# plt.show()
# exit()
# for u in range(10):
#     s_traj=[]
#     traj = np.loadtxt('traj/ntraj10000_Z1g1.0m1.0_'+str(u))
#     for k in range(len(traj)):
        
#         s_traj.append(s(np.array(traj[k,1:]),references,1))
#     plt.plot(traj[:,0],s_traj)
# plt.show()

