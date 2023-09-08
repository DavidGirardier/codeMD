from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt

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

def Vel(Lambda:float, q, i:int, dt:float):
    vel = Lambda*((q[i+1]-q[i])/dt) + (1.-Lambda)*((q[i]-q[i-1])/dt)
    return vel
def CountTraj(trajectory):
    dt = trajectory[:,0][1]
    nSteps = 0
    i=0
    while trajectory[:,0][i+1] > trajectory[:,0][i]:
        nSteps+= 1
        i+=1
    
    nTraj = int(len(trajectory[:,0])/nSteps)
    timeTraj = nSteps*dt
    return nTraj, nSteps, timeTraj


for name in ['TrajIntegratorCiccottiFPall1t100dt0_001']:
    trajectory = np.loadtxt(name)
    dt = trajectory[:,0][1]

    # q = [x for x in trajectory[:,1]]
    t = [x for x in trajectory[:,0]]

    realV = [x for x in trajectory[:,2]]
    G1 = [x for x in trajectory[:,3]]
    #G2 = [x for x in trajectory[:,3]]
    G2 = [x for x in trajectory[:,4]]


    vCentral = []
    vvp1Central = []
    vForward = []
    vvp1Forward = []
    vBackward = []
    vvp1Backward = []
    aCentral = []
    aForward = []
    aBackward = []
    qvCentral = []
    avCentral = []
    avForward = []
    avBackward = []
    a2vCentral = []
    qvForward = []
    qvBackward = []
    qqm1Central = []
    vqm1Central = []
    vqm1Forward = []
    vqm1Backward = []
    vGCentral = []
    vGBackward = []
    vGForward = []
    realVq = []
    realvvp1 = []
    vvp1 = []
    GG = []
    vfinite=[]
    vnew = []
    diff2 = []
    crossdiff = []
    vG1=[]
    vG2=[]
    vG1m1=[]
    vG2m1=[]
    CorrvG1=[]
    CorrvG2=[]
    CorrvG1m1=[]
    CorrvG2m1=[]
    qG1=[]
    qG2=[]
    qG1m1=[]
    qG2m1=[]
    qG1m2=[]
    qG2m2=[]
    CorrqG1=[]
    CorrqG2=[]
    CorrqG1m1=[]
    CorrqG2m1=[]
    CorrqG1m2=[]
    CorrqG2m2=[]


    vq = []
    uq = []
    vqm1 = []
    uqm1 = []
    vm1q = []
    um1q = []
    vu = []
    vum1 = []
    vv = []
    vvm1 = []
    uu = []
    uum1 = []
    corruumvv=[]
    corruuLambda=[]
    corruum1Lambda=[]
    corrvvLambda=[]
    corrvvm1Lambda=[]
    corruumvv=[]
    corruum1vvm1=[]
    corrvq=[]
    corruq=[]
    corrvqm1=[]
    corruqm1=[]
    corrvm1q=[]
    corrum1q=[]

    corrvu = []
    corrvum1 = []
    correlationLambda = []
    correlationG1Lambda = []
    correlationG2Lambda = []
    crossCorrelationLambda = []
    crossCorrelationG1Lambda = []
    crossCorrelationG2Lambda = []
    #listLambda = np.arange(0.0,1.1,0.1)
    listLambda = [0.5]

    nTraj, nSteps, timeTraj = CountTraj(trajectory)
    listTraj = trajectory[:,1][:].reshape(nTraj,nSteps+1)
    listvReal = np.array(realV).reshape(nTraj,nSteps+1)
    listG1 = np.array(G1).reshape(nTraj,nSteps+1)
    listG2 = np.array(G2).reshape(nTraj,nSteps+1)
    #print(listvReal)
  
    for l in listLambda:
        vfinite=[]

        for n in range(nTraj):

            #randomNumber1 = np.random.normal()
            for i in range(1,nSteps):
                v = Vel(l, listTraj[n], i, dt)
                vfinite.append(v)
                #print(listvReal[n][i])
                vG1.append(listvReal[n][i]*listG1[n][i])
                vG2.append(listvReal[n][i]*listG2[n][i])
                diff2.append((listvReal[n][i]-v)*(listvReal[n][i]-v))
                vu.append(v*listvReal[n][i])
                vv.append(listvReal[n][i]*listvReal[n][i])
                uu.append(v*v)
                vq.append(listvReal[n][i]*listTraj[n][i])
                uq.append(v*listTraj[n][i])

                qG1.append(listTraj[n][i]*listG1[n][i])
                qG2.append(listTraj[n][i]*listG2[n][i])

                if i>=2:
                    vm1 = Vel(l, listTraj[n], i-1, dt)
                    crossdiff.append((listvReal[n][i]-v)*(listvReal[n][i-1]-vm1))

                    vvm1.append(listvReal[n][i]*listvReal[n][i-1])
                    uum1.append(v*vm1)
                    vum1.append(v*listvReal[n][i-1])
                    vG1m1.append(listvReal[n][i]*listG1[n][i-1])
                    vG2m1.append(listvReal[n][i]*listG2[n][i-1])

                    vqm1.append(listvReal[n][i]*listTraj[n][i-1])
                    uqm1.append(v*listTraj[n][i-1])
                    vm1q.append(listvReal[n][i-1]*listTraj[n][i])
                    um1q.append(vm1*listTraj[n][i])


                    qG1m1.append(listTraj[n][i]*listG1[n][i-1])
                    qG2m1.append(listTraj[n][i]*listG2[n][i-1])

                if i>=3:
                    qG1m2.append(listTraj[n][i]*listG1[n][i-2])
                    qG2m2.append(listTraj[n][i]*listG2[n][i-2])

                    
            #vnew

        print(l)


        
        
        #correlationLambda.append(np.mean([(realV[i]-vfinite[i])*(realV[i]-vfinite[i])/(2.*1.*dt) for i in range(len(realV))]))
        correlationLambda.append(np.mean(diff2))

        correlationG1Lambda.append(np.mean(vG1))
        correlationG2Lambda.append(np.mean(vG2))
        crossCorrelationG1Lambda.append(np.mean(vG1m1))
        crossCorrelationG2Lambda.append(np.mean(vG2m1))
        
        #crossCorrelationLambda.append(np.mean([(realV[i]-vfinite[i])*(realV[i-1]-vfinite[i-1])/(2.*1.*dt) for i in range(1,len(realV))]))
        crossCorrelationLambda.append(np.mean(crossdiff))
        
        corrvu.append(np.mean(vu))
        corrvum1.append(np.mean(vum1))
        corruuLambda.append(np.mean(uu))
        corruum1Lambda.append(np.mean(uum1))
        corrvvLambda.append(np.mean(vv))
        corrvvm1Lambda.append(np.mean(vvm1))
        corrvq.append(np.mean(vq))
        corruq.append(np.mean(uq))
        corrvqm1.append(np.mean(vqm1))
        corruqm1.append(np.mean(uqm1))
        corrvm1q.append(np.mean(vm1q))
        corrum1q.append(np.mean(um1q))

        CorrqG1.append(np.mean(qG1))
        CorrqG2.append(np.mean(qG2))
        CorrqG1m1.append(np.mean(qG1m1))
        CorrqG2m1.append(np.mean(qG2m1))
        CorrqG1m2.append(np.mean(qG1m2))
        CorrqG2m2.append(np.mean(qG2m2))


        diff2 = []
        crossdiff = []
        vG1=[]
        vG2=[]
        vu=[]
        vum1=[]
        vv=[]
        vvm1=[]
        uu=[]
        uum1=[]
        vq=[]
        uq=[]
        vqm1 = []
        uqm1 = []
        vm1q = []
        um1q = []
        qG1=[]
        qG2=[]
        qG1m1=[]
        qG2m1=[]
        qG1m2=[]
        qG2m2=[]
        

#print(correlationLambda)
outputName = 'CorrelationVrealVfiniteVECall1t' + str(timeTraj) + 'dt' + str(dt)
np.savetxt(outputName, np.c_[listLambda, correlationLambda,crossCorrelationLambda,corrvu, corrvum1, correlationG1Lambda,correlationG2Lambda, crossCorrelationG1Lambda, crossCorrelationG2Lambda], fmt='%1.6E')     
# print('<a vC> = ' + str(np.mean(avCentral)))
# print('<a vF> = ' + str(np.mean(avBackward)))
outputName = 'meanVU'
np.savetxt(outputName, np.c_[listLambda, corruuLambda, corrvvLambda, corruum1Lambda, corrvvm1Lambda], fmt='%1.6E')     

outputName = 'meanVelPos'
np.savetxt(outputName, np.c_[listLambda, corrvq, corruq, corrvqm1, corruqm1, corrvm1q, corrum1q], fmt='%1.8E',header='l <vq> <uq> <vqm1> <uqm1> <vm1q> <um1q>')     

outputName = 'meanQG'
np.savetxt(outputName, np.c_[CorrqG1,CorrqG2,CorrqG1m1,CorrqG2m1,CorrqG1m2,CorrqG2m2], fmt='%1.6E',header='<qG1> <qG2> <qG1m1> <qG2m1> <qG1m2> <qG2m2>')     


# AC_Backward = autocorrelation(vBackward)
# AC_Central = autocorrelation(vCentral)
# np.savetxt('AutocorrelationVel', np.c_[AC_Backward,AC_Central], fmt='%1.8E')
exit()
for i in range(1,len(q)-1):
    if t[i+1]>t[i-1]:
        v = (q[i+1]-q[i])/(dt)
        vForward.append(v)
        qvForward.append(v*q[i])

for i in range(1,len(q)-1):
    if t[i+1]>t[i-1]:
        v = (q[i]-q[i-1])/(dt)
        vBackward.append(v)
        qvBackward.append(v*q[i])

print('<q vF> = ' + str(np.mean(qvForward)))
print('<q vC> = ' + str(np.mean(qvCentral)))
print('<q vB> = ' + str(np.mean(qvBackward)))
exit()
np.arange(0,1.1,0.05)
correlationvq=[]
for Lambda in np.arange(0,1.1,0.05):
    velocityQ=[]
    for i in range(1,len(q)-1):
        
        if t[i+1]>t[i-1]:
            velocityQ.append(Vel()*q[i-1])

    
    print('Lambda = ' + str(Lambda))
    print('<q v> = ' + str(np.mean(velocityQ)))
    correlationvq.append([Lambda, np.mean(velocityQ)])

outputName = 'Correlationvq'
np.savetxt(outputName, np.c_[correlationvq], fmt='%1.6E')   

# print('####### Ciccotti #######')
# print('<q vC> = ' + str(np.mean(qvCentral)))
# print('<vC qm1> = ' + str(np.mean(vqm1Central)))
# print('<vC G> = ' + str(np.mean(vGCentral)))
#  dprint('<realV q> = ' + str(np.mean(realVq)))


