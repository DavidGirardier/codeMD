import numpy as np
input_name='100shootingZWall_sd0_01'
traj = np.loadtxt(input_name)


for i in range(len(traj[:,1])):
    if traj[i,1] < -1.5 : traj[i,1]=traj[i,1]+2*np.pi

np.savetxt(input_name+'c', np.c_[traj])