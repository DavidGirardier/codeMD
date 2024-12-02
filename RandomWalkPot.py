import numpy as np
from scipy.fft import rfft, irfft, rfftfreq, fft, ifft, fftfreq, dct, idct
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import sys


def ForceDoubleWell(x:float):
    barrier = 5.
    Force = -4.0*barrier*x**3 + 4.0*barrier*x

    return Force

def PotWell(x:float):
    barrier = 2.
    Force = barrier*x**4 - 2.0*barrier*x**2

    return Force


D = 10.0
m = 1.0 
kT = 1.0

x0 = 0

delta_x = 0.1
dt = 0.001

numberOfTraj = 100.
num_step = 1000000
trajectory = []
time = []
t_max = 1000
t= 0.0
x = x0
while t < t_max:
    trajectory.append(x)
    time.append(t)
    
    x_possible1 = x + delta_x
    rij = D/(delta_x*delta_x)*np.exp(-(PotWell(x_possible1) - PotWell(x))/(2.*kT))
    
    x_possible2 = x - delta_x
    rji = D/(delta_x*delta_x)*np.exp(-(PotWell(x_possible2) - PotWell(x))/(2.*kT))

    Q = rij + rji
    
    u = np.random.rand()

    if (u*Q) <= rij :
        x = x_possible1
    else :
        x = x_possible2

    uprime = np.random.rand()

    tau = np.log(1/uprime)/Q
    t = t + tau

    # print('rij = ' + str(rij)) 
    # print('rji = ' + str(rji)) 
    # print('uQ = ' + str(u*Q))

    # if np.random.rand() <  acc : 
    #     x_new = x_possible
    # else : 
    #     x_new = x - jump
    
    #x = x_new
     
# fixed_times = [0.]
# fixed_positions = [trajectory[0]]
# counter = 0
# for i in range(1,len(trajectory)):

    
#     num_inter_set = int((time[i]-time[i-1])/dt)
#     #time_step = fixed_times[i-1]

    

#     for j in range(int(num_inter_set)):
#         counter += 1
#         fixed_times.append(counter*dt)
#         fixed_positions.append(trajectory[i-1])


# fixed_times = np.arange(start=0, stop=np.max(time), step=dt)

# # Create a function to find the last known position at each fixed time step
# def interpolate_position_at_fixed_times(times, positions, new_times):
#     # Initialize the result array
#     new_positions = np.zeros_like(new_times)
#     j = 0
#     for i, t in enumerate(new_times):
#         while j < len(times) and times[j] <= t:
#             j += 1
#         new_positions[i] = positions[j - 1] if j > 0 else positions[0]
#     return new_positions

# # Get the new interpolated positions
# fixed_positions = interpolate_position_at_fixed_times(time, trajectory, fixed_times)




# Example vector and variable
fixed_times = np.arange(start=0, stop=np.max(time), step=dt)

fixed_times2 = [0.]

fixed_positions = [trajectory[0]]
for i in range(len(trajectory)):
    # Calculate the absolute differences
    differences = np.abs(fixed_times - time[i])

    # Find the index of the minimum difference
    index_of_min_difference = np.argmin(differences)

    # Retrieve the closest element
    closest_time = fixed_times[index_of_min_difference]

    fixed_times2.append(closest_time)
    fixed_positions.append(trajectory[i])


outputName='randomWalk_D'+str(D)+'_deltax_'+str(delta_x)+'_interpolated'
np.savetxt(outputName, np.c_[fixed_times2,fixed_positions], fmt='%.8e')

outputName='randomWalk_D'+str(D)+'_deltax_'+str(delta_x)
np.savetxt(outputName, np.c_[time,trajectory], fmt='%.8e')