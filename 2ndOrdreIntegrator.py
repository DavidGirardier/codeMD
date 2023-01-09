import numpy as np
from typing import List, TypeVar, Tuple, Dict, Set

def autocorrelation(data):
    
    x = np.array(data) 

    # Mean
    mean = np.mean(data)

    # Variance
    var = np.var(data)

    # Normalized data
    ndata = data - mean

    acorr = np.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
    acorr = acorr / var / len(ndata)

    return acorr

def CicottiVandenEijdenFP(gamma:float, mass:float, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []
    g1:List[float] = []
    g2:List[float] = []
    
    v = initialVelocity 
    x = initialPosition
    sigma = np.sqrt(2.*kT*gamma/mass)
    for i in range(int(totalTime/timeStep)+1):
        trajectory.append(x)
        velocities.append(v)
        time.append(i*timeStep)

        randomNumber1 = np.random.normal()
        randomNumber2 = np.random.normal()

        #A=0.0
        A = -0.5*(timeStep**2.)*gamma*v + sigma*(timeStep**(3./2.))*(0.5*randomNumber1 + 1./(2.*np.sqrt(3.))*randomNumber2)
        x_new = x + timeStep*v + A
        v_new = v - timeStep*gamma*v + np.sqrt(timeStep)*sigma*randomNumber1 - gamma*A

        
        x = x_new
        v = v_new

        g1.append(randomNumber1)
        g2.append(randomNumber2)
    
    #print(np.mean(g2))
    #print(np.var(g2))   
        
    return time, trajectory, velocities 

def EulerMaruyamaFP(gamma:float, mass:float, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []

    
    v = initialVelocity 
    x = initialPosition
    sigma = np.sqrt(2.*kT*gamma/mass)
    for i in range(int(totalTime/timeStep)+1):
        trajectory.append(x)
        velocities.append(v)
        time.append(i*timeStep)

        randomNumber = np.random.normal()
        x_new = x + v*timeStep
        v_new = v - gamma*v*timeStep + np.sqrt(timeStep)*sigma*randomNumber

        
        x = x_new
        v = v_new
    return time, trajectory, velocities

def BAOAB(gamma:float, mass:float, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []
    g1:List[float] = []
    g2:List[float] = []
    
    v = initialVelocity 
    x = initialPosition
    p = mass*v
    for i in range(int(totalTime/timeStep)+1):
        trajectory.append(x)
        velocities.append(p/mass)
        time.append(i*timeStep)

        randomNumber1 = np.random.normal()
        

        p_half = p
        x_half = x + 0.5*timeStep*p_half/mass
        p_hat = np.exp(-timeStep*gamma)*p_half + np.sqrt(kT*(1. - np.exp(-2.*gamma*timeStep)))*np.sqrt(mass)*randomNumber1
        x_new = x_half + 0.5*timeStep*p_hat/mass
        p_new = p_hat
        
        x = x_new
        p = p_new

        g1.append(randomNumber1)
        
    
    #print(np.mean(g2))
    #print(np.var(g2))   
        
    return time, trajectory, velocities 
gamma = 10.  

mass = 1.
kT = 1.
x0 = 0.

dt=0.01
t=1.
PrintTraj = True
lenght = int(t/dt) + 1

numberOfTraj = 500.0

alltime = []
alltraj = []
allvel = []
x_final = []
v_final = []
for j in range(int(numberOfTraj)):
    v0 = np.sqrt(kT/mass) * np.random.normal()
    time, traj, vel = CicottiVandenEijdenFP(gamma, mass, kT, x0, v0, dt, t)

    if PrintTraj == True:
        alltime = alltime + time
        alltraj = alltraj + traj
        allvel = allvel + vel
    
    x_final.append(traj[-1])
    v_final.append(vel[-1])
    print('Traj'+str(j)+'     Done')


histo_x = np.histogram(x_final, np.arange(-1.5,1.5,0.05)) 
histo_v = np.histogram(v_final, np.arange(-5.*kT,5*kT, kT/10.))

v2 = [v*v for v in v_final]
x2 = [x*x for x in x_final]

v2_list = []
# for i in range(len(time)):
#     v2_list.append(np.mean([allvel[i + j*len(time)]*allvel[i + j*len(time)] for j in range(int(numberOfTraj))]))

#np.savetxt('v2Cicotti', np.c_[time,v2_list], fmt='%1.8E')

np.savetxt('qHistoCicotti', np.c_[histo_x[1][:-1],histo_x[0]/numberOfTraj], fmt='%1.8E')
np.savetxt('vHistoCicotti', np.c_[histo_v[1][:-1],histo_v[0]/numberOfTraj], fmt='%1.8E')
print('Cicotti-VandenEijden')
print('<x> = ' + str(np.mean(x_final)) + '\t <x^2> = ' + str(np.mean(x2)))
print('<v> = ' + str(np.mean(v_final)) + '\t <v^2> = ' + str(np.mean(v2)))
print('gamma = 2tkT/(m<x^2>) = ' + str(2.*t*kT/(np.mean(x2)*mass)) + '\t input gamma = ' + str(gamma))
print('mkT = 1/<v^2> = ' + str(1./(np.mean(v2))) + '\t input mkT = ' + str(mass*kT))
#np.savetxt('VAC_Ciccotti', np.c_[alltime, autocorrelation(allvel)], fmt='%1.8E')
histo_x = []
histo_v = []

outputName='TrajIntegratorCicotti'
np.savetxt(outputName, np.c_[alltime,alltraj,allvel], fmt='%1.8E')




alltime = []
alltraj = []
allvel = []
x_final = []
v_final = []
listVAC = []
for j in range(int(numberOfTraj)):
    v0 = np.sqrt(kT/mass) * np.random.normal()
    time, traj, vel = EulerMaruyamaFP(gamma, mass, kT, x0, v0, dt, t)
    listVAC.append(autocorrelation(vel))
    if PrintTraj == True:
        alltime = alltime + time
        alltraj = alltraj + traj
        allvel = allvel + vel
  
    # alltime = alltime + [time[i] for i in range(0, len(time), 10)]
    # alltraj = alltraj + [traj[i] for i in range(0, len(traj), 10)]
    # allvel = allvel + [vel[i] for i in range(0, len(vel), 10)]

    x_final.append(traj[-1])
    v_final.append(vel[-1])
    #print('Traj'+str(j)+'     Done')
#print(np.mean([alltraj[i] for i in range(0,len(alltraj), 1000)]))

# x_final = [alltraj[i-1] for i in range(lenght,len(alltraj)+1, lenght)]
# v_final = [allvel[i-1] for i in range(lenght,len(allvel)+1, lenght)]


histo_x = np.histogram(x_final, np.arange(-1.5,1.5,0.05)) 
histo_v = np.histogram(v_final, np.arange(-5.*kT,5*kT, kT/10.))

v2 = [v*v for v in v_final]
x2 = [x*x for x in x_final]

np.savetxt('qHistoEuler', np.c_[histo_x[1][:-1],histo_x[0]/numberOfTraj], fmt='%1.8E')
np.savetxt('vHistoEuler', np.c_[histo_v[1][:-1],histo_v[0]/numberOfTraj], fmt='%1.8E')
#np.savetxt('VAC_Euler', np.c_[alltime, autocorrelation(allvel)], fmt='%1.8E')


print(100*'#')
print('Euler-Maruyama')
print('<x> = ' + str(np.mean(x_final)) + '\t <x^2> = ' + str(np.mean(x2)))
print('<v> = ' + str(np.mean(v_final)) + '\t <v^2> = ' + str(np.mean(v2)))
print('gamma = 2tkT/(m<x^2>) = ' + str(2.*t*kT/(np.mean(x2)*mass)) + '\t input gamma = ' + str(gamma))
print('mkT = 1/<v^2> = ' + str(1./(np.mean(v2))) + '\t input mkT = ' + str(mass*kT))


# print(np.var([alltraj[i-1] for i in range(lenght,len(alltraj)+1, lenght)]))
# print(np.mean([allvel[i-1] for i in range(lenght,len(allvel)+1, lenght)]))
outputName='TrajIntegratorEuler'
np.savetxt(outputName, np.c_[alltime,alltraj,allvel], fmt='%1.8E')