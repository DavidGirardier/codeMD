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

def ForceDoubleWell(x:float):
    barrier = 10.
    Force = -4.0*barrier*x**3 + 4.0*barrier*x
    # Force = -100*(x+1)
    # alpha = 0.
    # Force = -2.*x + 3.*alpha*x*x
    #Force=0.0

    return Force

def gammaPos(x:float):
    barrier = 1.
    gammaq = barrier*x**4 - 2.0*barrier*x**2 +2.*barrier


    return gammaq

def deriveeGamma(x:float):
    barrier = 1.
    gammaq = 4*barrier*x**3 - 4.0*barrier*x


    return gammaq

def CicottiVandenEijdenFP(gamma:float, mass:float, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []
    g1:List[float] = []
    g2:List[float] = []

    meanq=0.
    meanqG1=0.
    meanvG1=0.
    meanqG2=0.
    meanG1=0.
    meanG2=0.
    varG1=0.
    varG2=0.
    meanG1G2=0.
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
        A = 0.5*(timeStep**2.)*(ForceDoubleWell(x)/mass-gamma*v) + sigma*(timeStep**(3./2.))*(0.5*randomNumber1 + 1./(2.*np.sqrt(3))*randomNumber2)
        x_new = x + timeStep*v + A
        v_new = v - timeStep*gamma*v + 0.5*timeStep*(ForceDoubleWell(x_new)+ForceDoubleWell(x))/mass + np.sqrt(timeStep)*sigma*randomNumber1 - gamma*A

        
        x = x_new
        v = v_new

    
    return time, trajectory, velocities, g1, g2


def CicottiVandenEijdenGammaPos(mass:float, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []
    g1:List[float] = []
    g2:List[float] = []

    v = initialVelocity 
    x = initialPosition

    for i in range(int(totalTime/timeStep)+1):
        trajectory.append(x)
        velocities.append(v)
        time.append(i*timeStep)

        randomNumber1 = np.random.normal()
        randomNumber2 = np.random.normal()


        sigma = np.sqrt(2.*kT*gammaPos(x)/mass)
        A = 0.5*(timeStep**2.)*(ForceDoubleWell(x)/mass-gammaPos(x)*v) + sigma*(timeStep**(3./2.))*(0.5*randomNumber1 + 1./(2.*np.sqrt(3))*randomNumber2)
        x_new = x + timeStep*v + A
        sigma = np.sqrt(2.*kT*gammaPos(x_new)/mass)
        v_new = v - timeStep*gammaPos(x_new)*v + 0.5*timeStep*(ForceDoubleWell(x_new)+ForceDoubleWell(x))/mass + np.sqrt(timeStep)*sigma*randomNumber1 - gammaPos(x_new)*A

        
        x = x_new
        v = v_new

    
    return time, trajectory, velocities, g1, g2

def EulerMaruyamaFP(gamma:float, mass:float, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []
    g:List[float] = []

    
    v = initialVelocity 
    x = initialPosition
    sigma = np.sqrt(2.*kT*gamma/mass)
    for i in range(int(totalTime/timeStep)+1):
        trajectory.append(x)
        velocities.append(v)
        time.append(i*timeStep)

        randomNumber = np.random.normal()
        x_new = x + v*timeStep
        v_new = v - gamma*v*timeStep + timeStep*ForceDoubleWell(x)/mass + np.sqrt(timeStep)*sigma*randomNumber

        g.append(randomNumber)
        x = x_new
        v = v_new
    return time, trajectory, velocities, g

def Milstein(mass:float, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []
    g:List[float] = []

    
    v = initialVelocity 
    x = initialPosition
    
    for i in range(int(totalTime/timeStep)+1):
        trajectory.append(x)
        velocities.append(v)
        time.append(i*timeStep)

        randomNumber = np.random.normal()
        x_new = x + v*timeStep
        sigma = np.sqrt(2.*kT*gammaPos(x_new)/mass)
        v_new = v - gammaPos(x_new)*v*timeStep + timeStep*ForceDoubleWell(x)/mass + np.sqrt(timeStep)*sigma*randomNumber \
              - 0.5*kT/(gammaPos(x_new)*gammaPos(x_new)*mass)*deriveeGamma(x_new)*timeStep*(randomNumber*randomNumber-1.0)

        g.append(randomNumber)
        x = x_new
        v = v_new
    return time, trajectory, velocities, g
    #v' = v + (F/m)*dt - g*v*dt + sqrt(dt*2*D)*G + 0.5*(dD/dx)*(G^2-1)*dt


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
        
        time.append(i*timeStep)

        randomNumber1 = np.random.normal()
        

        p_half = p + 0.5*timeStep*ForceDoubleWell(x)
        x_half = x + 0.5*timeStep*p_half/mass
        p_hat = np.exp(-timeStep*gamma)*p_half + np.sqrt(kT*(1. - np.exp(-2.*gamma*timeStep)))*np.sqrt(mass)*randomNumber1
        x_new = x_half + 0.5*timeStep*p_hat/mass
        p_new = p_hat + 0.5*timeStep*ForceDoubleWell(x_new)
        trajectory.append(x)
        velocities.append(p_new/mass)
        x = x_new
        p = p_new

        g1.append(randomNumber1)
        
        
    
    #print(np.mean(g2))
    #print(np.var(g2))   
        
    return time, trajectory, velocities, g1

def OBABO(gamma:float, mass:float, kT:float, initialPosition:float, initialVelocity:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    time:List[float] = []
    g1:List[float] = []
    g2:List[float] = []
    
    v = initialVelocity 
    x = initialPosition
    p = mass*v
    for i in range(int(totalTime/timeStep)+1):
        
        time.append(i*timeStep)

        randomNumber1 = np.random.normal()
        randomNumber2 = np.random.normal()
        

        p_half = np.exp(-0.5*timeStep*gamma)*p + np.sqrt(kT*(1. - np.exp(-gamma*timeStep)))*np.sqrt(mass)*randomNumber1
        p_half_hat = p_half + 0.5*timeStep*ForceDoubleWell(x)
        x_new = x + timeStep*1./mass*p_half_hat
        p_new_hat = p_half_hat + 0.5*timeStep*ForceDoubleWell(x_new)
        p_new = np.exp(-0.5*timeStep*gamma)*p_new_hat + np.sqrt(kT*(1. - np.exp(-gamma*timeStep)))*np.sqrt(mass)*randomNumber2


        trajectory.append(x)
        velocities.append(p_new/mass)
        x = x_new
        p = p_new

        g1.append(randomNumber1)
        g2.append(randomNumber2)

    return time, trajectory, velocities, g1, g2

gamma = 1.

mass = 1.5
kT = 1.
x0 = 0.

dt=0.001
t=1.
PrintTraj = True
lenght = int(t/dt) + 1

numberOfTraj = 500.

fraction = 5.

every = 10

alltime = []
alltraj = []
allvel = []
allg1 = []
allg2 = []
x_final = []
v_final = []

strdt=''
for l in str(dt):
    
    if l == '.':
        strdt+='_'
    else:
        strdt+=l

countFrac=0
for j in range(int(numberOfTraj)):

    
    v0 = np.sqrt(kT/mass) * np.random.normal()
    #time, traj, vel, g1 = EulerMaruyamaFP(gamma, mass, kT, x0, v0, dt, t)
    #time, traj, vel, g1, _ = CicottiVandenEijdenFP(gamma, mass, kT, x0, v0, dt, t)
    #time, traj, vel, g1, _ = CicottiVandenEijdenGammaPos(mass, kT, x0, v0, dt, t)
    time, traj, vel, g1 = Milstein(mass, kT, x0, v0, dt, t)

    if PrintTraj == True:
        alltime = alltime + time[::every]
        alltraj = alltraj + traj[::every]
        allvel = allvel + vel[::every]
        # allg1 = allg1 + g1
        #allg2 = allg2 + g2
    x_final.append(traj[-1])
    v_final.append(vel[-1])
    print('Traj'+str(j)+'     Done')

    if (j+1) % (int(numberOfTraj/fraction)) == 0:

        countFrac = countFrac + 1
        #outputName='100TrajVECg' + str(gamma) + 'm' + str(mass) + '_' + str(countFrac)
        outputName='500TrajMilsteing_gammasmallpos'+ 'm' + str(mass) + '_' + str(countFrac)
        #outputName='Eulerm120g1_5DW7FullkTdt0_001x20_Ergodic_'+str(countFrac)
        np.savetxt(outputName, np.c_[alltime,alltraj,allvel], fmt='%1.8E')


        v2 = [v*v for v in allvel]
        x = [q for q in alltraj]
        x2 = [q*q for q in alltraj]
        print('<v> = ' + str(np.mean(allvel)) + '\t <v^2> = ' + str(np.mean(v2)))
        print('mkT = 1/<v^2> = ' + str(1./(np.mean(v2))) + '\t input mkT = ' + str(mass*kT))
        print('<x^2> - <x>^2 = ' + str(np.mean(x2) - np.mean(x)*np.mean(x)))
        alltime = []
        alltraj = []
        allvel = []
print(outputName)
exit()
histo_x = np.histogram(x_final, np.arange(-1.5,1.5,0.05)) 
histo_v = np.histogram(v_final, np.arange(-5.*kT,5*kT, kT/10.))

v2 = [v*v for v in allvel]
#x2 = [x*x for x in x_final]

v2_list = []
# for i in range(len(time)):
#     v2_list.append(np.mean([allvel[i + j*len(time)]*allvel[i + j*len(time)] for j in range(int(numberOfTraj))]))

#np.savetxt('v2Cicotti', np.c_[time,v2_list], fmt='%1.8E')

np.savetxt('qHistoCicotti', np.c_[histo_x[1][:-1],histo_x[0]/numberOfTraj], fmt='%1.8E')
np.savetxt('vHistoCicotti', np.c_[histo_v[1][:-1],histo_v[0]/numberOfTraj], fmt='%1.8E')
print('Cicotti-VandenEijden')
#print('<x> = ' + str(np.mean(x_final)) + '\t <x^2> = ' + str(np.mean(x2)))
print('<v> = ' + str(np.mean(allvel)) + '\t <v^2> = ' + str(np.mean(v2)))

#print('gamma = 2tkT/(m<x^2>) = ' + str(2.*t*kT/(np.mean(x2)*mass)) + '\t input gamma = ' + str(gamma))
print('mkT = 1/<v^2> = ' + str(1./(np.mean(v2))) + '\t input mkT = ' + str(mass*kT))
#np.savetxt('VAC_Ciccotti', np.c_[alltime, autocorrelation(allvel)], fmt='%1.8E')
histo_x = []
histo_v = []

outputName='Traj500IntegratorEulerSimilarFullm120g2DW7'
np.savetxt(outputName, np.c_[alltime,alltraj,allvel,allg1], fmt='%1.8E')




# alltime = []
# alltraj = []
# allvel = []
# allg = []
# x_final = []
# v_final = []
# listVAC = []
# for j in range(int(numberOfTraj)):
#     v0 = np.sqrt(kT/mass) * np.random.normal()
#     time, traj, vel, g = EulerMaruyamaFP(gamma, mass, kT, x0, v0, dt, t)
#     listVAC.append(autocorrelation(vel))
#     if PrintTraj == True:
#         alltime = alltime + time
#         alltraj = alltraj + traj
#         allvel = allvel + vel
#         allg = allg + g
  
#     # alltime = alltime + [time[i] for i in range(0, len(time), 10)]
#     # alltraj = alltraj + [traj[i] for i in range(0, len(traj), 10)]
#     # allvel = allvel + [vel[i] for i in range(0, len(vel), 10)]

#     x_final.append(traj[-1])
#     v_final.append(vel[-1])
#     #print('Traj'+str(j)+'     Done')
# #print(np.mean([alltraj[i] for i in range(0,len(alltraj), 1000)]))

# # x_final = [alltraj[i-1] for i in range(lenght,len(alltraj)+1, lenght)]
# # v_final = [allvel[i-1] for i in range(lenght,len(allvel)+1, lenght)]


# histo_x = np.histogram(x_final, np.arange(-1.5,1.5,0.05)) 
# histo_v = np.histogram(v_final, np.arange(-5.*kT,5*kT, kT/10.))

# v2 = [v*v for v in v_final]
# x2 = [x*x for x in x_final]

# np.savetxt('qHistoEuler', np.c_[histo_x[1][:-1],histo_x[0]/numberOfTraj], fmt='%1.8E')
# np.savetxt('vHistoEuler', np.c_[histo_v[1][:-1],histo_v[0]/numberOfTraj], fmt='%1.8E')
# #np.savetxt('VAC_Euler', np.c_[alltime, autocorrelation(allvel)], fmt='%1.8E')


# print(100*'#')
# print('Euler-Maruyama')
# print('<x> = ' + str(np.mean(x_final)) + '\t <x^2> = ' + str(np.mean(x2)))
# print('<v> = ' + str(np.mean(v_final)) + '\t <v^2> = ' + str(np.mean(v2)))
# print('gamma = 2tkT/(m<x^2>) = ' + str(2.*t*kT/(np.mean(x2)*mass)) + '\t input gamma = ' + str(gamma))
# print('mkT = 1/<v^2> = ' + str(1./(np.mean(v2))) + '\t input mkT = ' + str(mass*kT))


# # print(np.var([alltraj[i-1] for i in range(lenght,len(alltraj)+1, lenght)]))
# # print(np.mean([allvel[i-1] for i in range(lenght,len(allvel)+1, lenght)]))
# outputName='TrajIntegratorEuler'
# np.savetxt(outputName, np.c_[alltime,alltraj,allvel, allg], fmt='%1.8E')



# # alltime = []
# # alltraj = []
# # allvel = []
# # allg = []
# # for j in range(int(numberOfTraj)):
# #     v0 = np.sqrt(kT/mass) * np.random.normal()
# #     time, traj, vel, g = BAOAB(gamma, mass, kT, x0, v0, dt, t)

# #     if PrintTraj == True:
# #         alltime = alltime + time
# #         alltraj = alltraj + traj
# #         allvel = allvel + vel
# #         allg = allg + g
  
# #     # alltime = alltime + [time[i] for i in range(0, len(time), 10)]
# #     # alltraj = alltraj + [traj[i] for i in range(0, len(traj), 10)]
# #     # allvel = allvel + [vel[i] for i in range(0, len(vel), 10)]

    





# # outputName='TrajIntegratorBAOAB'
# # np.savetxt(outputName, np.c_[alltime,alltraj,allvel, allg], fmt='%1.8E')