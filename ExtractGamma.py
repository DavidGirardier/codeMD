import numpy as np

from scipy.fftpack import fft, ifft, ifftshift

import matplotlib.pyplot as plt



def dFdq(x:float):
    barrier = 10
    der = 4.0*barrier*x**3 - 4.0*barrier*x
    #Force = -9.81
    # alpha = 0.
    # Force = -2.*x + 3.*alpha*x*x
    #Force=0.0
    #der = 0.
    return der

# inputfile = input('Trajectory File:')
# trajectories = np.loadtxt(inputfile, max_rows=2)
inputfile= 'EulerDW10kTdt_0.0001_g0.5m10.0every10_1'
unzoomedFactor = 1

trajectory = np.loadtxt(inputfile, skiprows=0, max_rows=10)
dt = trajectory[1,0]-trajectory[0,0]
print(dt)
m = 10.
kT = 1.0


#dt=0.001
numberOfTraj = 1
tFile = 100
nLine = tFile/dt
newdt = dt * unzoomedFactor

matrixXAC = []
matrixVAC = []

for i in range(numberOfTraj):
    trajectory = np.loadtxt(inputfile, skiprows=int(nLine)*i, max_rows=int(nLine)+1)
    print(trajectory)
    unzoomedPos = [x for x in trajectory]
    unzoomedVel = [(trajectory[i+1*unzoomedFactor,1]-trajectory[i-1*unzoomedFactor,1])/(2.*dt*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    unzoomedVel = np.array(unzoomedVel)

    unzoomedAcc = [(trajectory[i+1*unzoomedFactor,1]-2.*trajectory[i,1]+trajectory[i-1*unzoomedFactor,1])/(dt*dt*unzoomedFactor*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
    unzoomedAcc2 = [(unzoomedVel[i+1*unzoomedFactor]-unzoomedVel[i-1*unzoomedFactor])/(2.0*dt*unzoomedFactor) for i in range(1*unzoomedFactor,len(unzoomedVel)-1*unzoomedFactor,unzoomedFactor)]
    #realAcc = [a for a in trajectory[:,3]]
    realAcc = np.zeros(len(unzoomedVel))
    realVel = [v for v in trajectory[1:-1,2]]
    dFdq_t= [dFdq(x) for x in trajectory[1:-1,1]] 
    
    
    unzoomedAcc = np.array(unzoomedAcc)
    unzoomedPos = np.array(unzoomedPos)
    unzoomedAcc2 = np.array(unzoomedAcc2)
    realAcc = np.array(realAcc)
    realVel = np.array(realVel)
    dFdq_t = np.array(dFdq_t)
   
    # a = kT/m
    # b = 2.0*(np.mean(unzoomedVel*dFdq_t/m) + kT/m)
    # #c = np.mean(dFdq_t*dFdq_t)/(m*m) - np.mean(unzoomedAcc*unzoomedAcc)
    # c = np.mean(dFdq_t*dFdq_t)/(m*m) - np.mean(unzoomedAcc*unzoomedAcc*dt)
    #c = np.mean(dFdq_t*dFdq_t)/(m*m) - np.mean(unzoomedAcc2*unzoomedAcc2*dt)
    #c = np.mean(dFdq_t*dFdq_t)/(m*m) - np.mean(realAcc*realAcc)


    #delta = (2.0*np.mean(unzoomedVel*dFdq_t/m) + 2.0*kT/m)**2 - 4.0*kT/m*(np.mean(dFdq_t*dFdq_t)/(m*m) - np.mean(unzoomedAcc*unzoomedAcc)) 

    # g_p = (-b + np.sqrt(b*b-4.0*a*c))/(2.*a)
    # g_m = (-b - np.sqrt(b*b-4.0*a*c))/(2.*a)

gamma = 0.0
# G = (unzoomedAcc + gamma * realVel) / np.sqrt(dt)
# unzoomedAcctest = - gamma * realVel + G

# G = (unzoomedAcc + gamma * unzoomedVel) * np.sqrt(dt)
# unzoomedAcctest = - gamma * unzoomedVel + G

# G = (unzoomedAcc + gamma * unzoomedVel) * np.sqrt(dt) *np.sqrt(6.)/2.0
# unzoomedAcctest = - gamma * unzoomedVel + G

# unzoomedAcctest = - gamma * unzoomedVel + (unzoomedAcc + gamma * unzoomedVel) * np.sqrt(dt)

# G = (unzoomedAcc + gamma * unzoomedVel) * np.sqrt(dt)
# unzoomedAcctest = - gamma * unzoomedVel + (1.+gamma*(2./3.))*G

G = (unzoomedAcc + gamma * unzoomedVel + dFdq_t/m) * np.sqrt(dt) *np.sqrt(6.)/2.0
unzoomedAcctest = - gamma * unzoomedVel - dFdq_t/m + G

plt.plot([t*newdt for t in range(len(unzoomedAcc))], unzoomedAcc, label='finite diff pos')
plt.plot([t*newdt for t in range(len(unzoomedAcctest))], unzoomedAcctest, label='corrected')
plt.plot([t*newdt for t in range(len(realAcc))], realAcc, label='real')
plt.legend()
plt.show()
sigma2 = 2.0*kT/m*gamma*dt
corrV2 = (2.0/3.0)*2.0*kT/m*gamma*dt 
print(corrV2)
# meanU2 = np.mean(unzoomedVel*unzoomedVel)
# meanAcc_corr = gamma*gamma*(meanU2+corrV2) + (np.mean(gamma*unzoomedAcc*unzoomedVel) + np.mean(unzoomedAcc*unzoomedAcc) \
#             + gamma*gamma*(meanU2+corrV2))*dt - (gamma*np.mean(unzoomedAcc*unzoomedVel) + gamma*gamma*(meanU2+corrV2))*np.sqrt(dt)


# unzoomedVel = realVel
# meanV2 = np.mean(unzoomedVel*unzoomedVel)
# meanAcc_corr = gamma*gamma*(meanV2) + (np.mean(gamma*unzoomedAcc*unzoomedVel) + np.mean(unzoomedAcc*unzoomedAcc) \
#             + gamma*gamma*(meanV2))*dt - (gamma*np.mean(unzoomedAcc*unzoomedVel) + gamma*gamma*(meanV2))*np.sqrt(dt)

a = kT/m
b = 2.0*(np.mean(unzoomedVel*dFdq_t/m) + kT/m)
#c = np.mean(dFdq_t*dFdq_t)/(m*m) - np.mean(realAcc*realAcc)
c = np.mean(dFdq_t*dFdq_t)/(m*m) - np.mean(unzoomedAcctest*unzoomedAcctest)
#c = np.mean(dFdq_t*dFdq_t)/(m*m) - meanAcc_corr

g_p = (-b + np.sqrt(b*b-4.0*a*c))/(2.*a)
g_m = (-b - np.sqrt(b*b-4.0*a*c))/(2.*a)

print('<acc> = ' + str(np.mean(unzoomedAcc*unzoomedAcc)))
print('<acc> = ' + str(np.mean(realAcc*realAcc)))
print('gamma+ = ' + str(g_p))
print('gamma- = ' + str(g_m))
exit()


plt.plot([t*newdt for t in range(len(unzoomedAcc))], unzoomedAcc, label='finite diff pos')
plt.plot([t*newdt for t in range(len(unzoomedAcc2))], unzoomedAcc2, label='finite diff vel')
plt.plot([t*newdt for t in range(len(realAcc))], realAcc, label='real')
plt.legend()
plt.show()
        


#