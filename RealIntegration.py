import scipy.integrate as integrate
import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt



traj_input = 'dcom_asso'
#traj = np.loadtxt('../'+traj_input)
traj = np.loadtxt(traj_input)

#memory_input = '../memory/Kernel_split_' +traj_input+ 'amidpoint'
memory_input = "Kernel_split_cv_commidpoint"
memory = np.loadtxt(memory_input)

dt=0.002

ev=1

vel =unzoomedVel = [(traj[i+1*ev,1]-traj[i-1*ev,1])/(2.*dt*ev) for i in range(1*ev,len(traj)-1*ev,ev)]

print(np.mean(vel))
print(1/np.var(vel))


print(np.floor(len(vel)/len(memory[:,1])))
block = np.floor(len(vel)/len(memory[:,1]))
size_block = int(len(memory))

real_integration = []
real_vel = []
block = int(block)
for i in range(block):

    integrand = memory[:,1]*vel[size_block*i:size_block*(i+1)]


    integration = integrate.cumtrapz(integrand,memory[:,0])
    
    real_integration.append(integration[-1])
    real_vel.append(vel[size_block*i])

    

def func(g,v):
    return (g*v)

popt, pcov = optimize.curve_fit(func, real_vel, real_integration, p0=[0.])


plt.plot(real_vel,real_integration,'bo',markersize=5)
print(popt)
f=lambda x: popt*x


val = np.linspace(min(real_vel),max(real_vel),100)
plt.plot(val, f(val))
plt.show()

perr = np.sqrt(np.diag(pcov))
                 
outputName = 'RealIntegration_'+traj_input
np.savetxt(outputName, np.c_[real_vel,real_integration,real_vel*popt, real_vel*perr],header=str(popt)+'*v, perr = '+str(perr), fmt='%1.8E')