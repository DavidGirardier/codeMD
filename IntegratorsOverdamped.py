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
    # barrier = 5.
    # Force = -4.0*barrier*x**3 + 4.0*barrier*x
    Force = -5000*x
    #Force = -9.81
    # alpha = 0.
    # Force = -2.*x + 3.*alpha*x*x
    #Force=0.0

    return Force

def gammaPos(x:float):
    barrier = 10.
    gammaq = barrier*x**4 - 2.0*barrier*x**2 +2.*barrier


    return gammaq
    #return 1.0

def deriveeGamma(x:float):
    barrier = 1.
    gammaq = 4*barrier*x**3 - 4.0*barrier*x


    #return gammaq
    return 0.0



def EulerMaruyamaFP(gamma:float, mass:float, kT:float, initialPosition:float, timeStep:float, totalTime:float):
    trajectory:List[float] = []
    velocities:List[float] = []
    acceleration=[]
    time:List[float] = []
    g:List[float] = []

    

    x = initialPosition
    D = kT/(gamma*mass)
    for i in range(int(totalTime/timeStep)+1):
        trajectory.append(x)
        

        time.append(i*timeStep)

        randomNumber = np.random.normal()
        x_new = x + timeStep*ForceDoubleWell(x)/gamma + np.sqrt(2.*D*timeStep)*randomNumber

        x = x_new
        
    return time, trajectory



gamma = 10

mass = 1.
kT = 1.
x0 = -0.

dt=0.001
t=10000
PrintTraj = True
lenght = int(t/dt) + 1

numberOfTraj = 1.

fraction = 1.

every = 1

alltime = []
alltraj = []
allvel = []
allacc = []
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

    
    
    time, traj= EulerMaruyamaFP(gamma, mass, kT, x0, dt, t)
    #time, traj, vel, g1 = CicottiVandenEijdenFP(gamma, mass, kT, x0, v0, dt, t)
    #time, traj, vel, g1, _ = CicottiVandenEijdenGammaPos(mass, kT, x0, v0, dt, t)
    #time, traj, vel, g1 = Milstein(mass, kT, x0, v0, dt, t)

    if PrintTraj == True:
        alltime = alltime + time[::every]
        alltraj = alltraj + traj[::every]
    x_final.append(traj[-1])

    print('Traj'+str(j)+'     Done')

    if (j+1) % (int(numberOfTraj/fraction)) == 0:

        countFrac = countFrac + 1
        #outputName='500TrajVECg' + str(gamma) + 'm' + str(mass) + '_' + str(countFrac)
        #outputName='Well_5TrajMilstein_gammasmallpos'+ 'm' + str(mass) + '_' + str(countFrac)
        #outputName='Eulerm120g1_5DW7FullkTdt0_001x20_Ergodic_'+str(countFrac)
        # outputName='100EM_OLE_g'+str(gamma)
        # np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%1.8E')
        # outputName='3digit_100EM_OLE_g'+str(gamma)
        # np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%.3f')
        # outputName='2digit_100EM_OLE_g'+str(gamma)
        # np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%.2f')
        # outputName='1digit_100EM_OLE_g'+str(gamma)
        # np.savetxt(outputName, np.c_[alltime,alltraj], fmt='%.1f')
        
        np.savetxt('HarmoD1', np.c_[alltime,alltraj], fmt='%1.8E')

        
#print(outputName)
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