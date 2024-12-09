import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, ifftshift
import glob
def autocorrelation(data):
    
    x = np.array(data) 

    # Mean
    mean = np.mean(data)

    # Variance
    var = np.var(data)

    # Normalized data
    ndata = data - mean
    #ndata = data - data[0]
    acorr = np.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
    acorr = acorr / var / len(ndata)

    return acorr

def autocorrelation0(data):
    
    x = np.array(data) 

    # Mean
    mean = np.mean(data)

    # Variance
    var = np.var(data)

    # Normalized data
    ndata = data #- mean
    #accor = np.empty(0)
    acorr = []
    #acorr = np.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
    for i in range(len(data)):
        inst = ndata[0]*ndata[i]
        #accor = np.concatenate((accor,inst))
        acorr.append(inst)
    #acorr = acorr / var / len(ndata)
    acorr = acorr / acorr[0] 

    return acorr

def autocorrelationFFT(x):
    xp = ifftshift((x - np.average(x))/np.std(x))
    n, = xp.shape
    xp = np.r_[xp[:n//2], np.zeros_like(xp), xp[n//2:]]
    f = fft(xp)
    p = np.absolute(f)**2
    pi = ifft(p)
    return np.real(pi)[:n//2]/(np.arange(n//2)[::-1]+n//2)

def VAC0(data):
    max_len = max(len(t) for t in data)
    longest_traj_index = max(range(len(data)), key=lambda i: len(data[i]))
    longestTime = matrixTIME[longest_traj_index]
    numberOfTraj= len(data[:,0])
    # print(longestTime)
    # exit()
    acorr = []
    c0=0.
    for t in range(max_len):
        c_t = 0.
        for i in range(numberOfTraj):
            if t == 0:
                c0 = c0 + data[i,t]*data[i,t]
            c_t = c_t + data[i,0]*data[i,t]

        acorr.append(c_t)

    return acorr/c0


def DissipationWork(mQ,mV):
    numberOfTraj= len(matrixV[:,0])
    matrixWork = []
    
    for i in range(numberOfTraj):
        allWork = []
        pos = mQ[i,:]
        vel = mV[i,:]
        Work = 0.
        for j in range(0,len(pos)-1):
            dx = abs(pos[j+1]- pos[j])
            Work = Work + abs(vel[j]) * dx 
            allWork.append(Work)
        matrixWork.append(allWork)
    return np.array(matrixWork)
    

folder='traj/'
folder_out='analysis/'
inputfile= 'ntraj10000_Z1g5.0m1.0'


files= glob.glob(folder+inputfile+'*')
unzoomedFactor = 1
dt = 0.001
#print(files)

newdt = dt * unzoomedFactor


ratio_list = np.linspace(0,1,11)

for ratio in ratio_list:
    print(str(ratio))
    matrixTIME=[]
    matrixVAC=[]
    matrixQ=[]
    matrixV=[]
    matrixV2=[]

    for j in files:

        Twodim = np.array(np.loadtxt(j))
        time=Twodim[:,0]
        x=Twodim[:,1]
        y=Twodim[:,2]


        combination = -1.0*(ratio * x + (1.0-ratio)*y)
        trajectory=np.column_stack((time, combination))
        # print(trajectory)
        # print(trajectory[1,1])
        # exit()
        unzoomedVel = [(trajectory[i+1*unzoomedFactor,1]-trajectory[i-1*unzoomedFactor,1])/(2.*dt*unzoomedFactor) for i in range(1*unzoomedFactor,len(trajectory)-1*unzoomedFactor,unzoomedFactor)]
        
        matrixTIME.append(trajectory[1:-1,0])
        matrixQ.append(trajectory[1:-1,1])
        # matrixVAC.append(autocorrelation0(unzoomedVel))
        matrixV.append(unzoomedVel)
        #matrixV2.append(unzoomedVel*unzoomedVel)

        
        
        trajectory = []

    max_len = max(len(t) for t in matrixV)
    longest_traj_index = max(range(len(matrixV)), key=lambda i: len(matrixV[i]))
    longestTime = matrixTIME[longest_traj_index]

    padded_vel = [np.pad(t, (0, max_len - len(t)), 'constant') for t in matrixV]
    padded_pos = [np.pad(t, (0, max_len - len(t)), 'constant') for t in matrixQ]

    matrixV = np.array(padded_vel)
    matrixQ = np.array(padded_pos)
    numberOfTraj= len(matrixV[:,0])
    vac0 = VAC0(matrixV)
    print(matrixV)

    print(np.mean(np.multiply(matrixV,matrixV),axis=0))


    meanV2 = np.mean(np.multiply(matrixV,matrixV),axis=0)
    stdV2 = np.std(np.multiply(matrixV,matrixV),axis=0)
    outputName=folder_out+'VAC0'+inputfile+'_ratio_'+str(ratio)[0:4]
    np.savetxt(outputName, np.c_[longestTime, vac0], fmt='%1.8E')
    outputName=folder_out+'V2'+inputfile+'_ratio_'+str(ratio)[0:4]
    np.savetxt(outputName, np.c_[longestTime, meanV2,stdV2/np.sqrt(numberOfTraj)], fmt='%1.8E')

    dissip = DissipationWork(matrixQ,matrixV)
    meanWd = np.mean(dissip,axis=0)
    stdWd = np.std(dissip,axis=0)
    outputName=folder_out+'Wd'+inputfile+'_ratio_'+str(ratio)[0:4]
    np.savetxt(outputName, np.c_[longestTime[:-1], meanWd,stdWd/np.sqrt(numberOfTraj)], fmt='%1.8E')

    V20=meanV2[0]
    outputName=folder_out+'V2norm'+inputfile+'_ratio_'+str(ratio)[0:4]
    np.savetxt(outputName, np.c_[longestTime, meanV2/V20,stdV2/np.sqrt(numberOfTraj)], fmt='%1.8E')
# print(dissip)
# plt.plot(longestTime[:-1],np.mean(dissip,axis=0))
# plt.show()
# exit()
# plt.plot(longestTime,vac0)

# plt.show()
# plt.plot(longestTime,meanV2)
# plt.show()
exit()



#print(matrixVAC)

# plt.plot(matrixTIME[0], matrixVAC[0])
# plt.plot(matrixTIME[1], matrixVAC[1])

# min_len = min(len(t) for t in matrixVAC)
# shorthest_traj_index = min(range(len(matrixVAC)), key=lambda i: len(matrixVAC[i]))
# shortestTime = matrixTIME[shorthest_traj_index]
# short_VAC = [t[0:min_len] for t in matrixVAC]
# mean_VAC = np.mean(short_VAC, axis=0)
#plt.plot(shortestTime, mean_VAC)


max_len = max(len(t) for t in matrixVAC)
longest_traj_index = max(range(len(matrixVAC)), key=lambda i: len(matrixVAC[i]))
longestTime = matrixTIME[longest_traj_index]




long_VAC = [np.pad(t, (0, max_len - len(t)), 'constant') for t in matrixVAC]
mean_VAC = np.mean(long_VAC, axis=0)
std_VAC = np.std(long_VAC, axis=0)

# plt.plot(longestTime,matrixVAC[0])
# plt.plot(longestTime,matrixVAC[1])
# plt.plot(longestTime,matrixVAC[3])
# plt.plot(longestTime,matrixVAC[4])
# plt.show()

# exit()


outputName='VAC0'+inputfile
np.savetxt(outputName, np.c_[longestTime, mean_VAC, std_VAC/np.sqrt(len(files))], fmt='%1.8E')

plt.plot(longestTime, mean_VAC)



plt.xlabel('t')
plt.ylabel('Vac0')

plt.legend()
plt.show()
outputName='VAC0'+inputfile
np.savetxt(outputName, np.c_[longestTime, mean_VAC, std_VAC/np.sqrt(len(files))], fmt='%1.8E')

exit()

# matrixVAC
# print([matrixXAC[i][-1] for i in range(numberOfTraj)])
# print(np.var([matrixXAC[i][-1] for i in range(numberOfTraj)]))
# XAC = np.mean(matrixXAC, axis=0)
VAC = np.mean(matrixVAC, axis=0)
# XACvariance = np.std(matrixXAC, axis=0)
VACvariance = np.std(matrixVAC, axis=0)
#np.savetxt(outputName, np.c_[[t*newdt for t in range(int(tFile/newdt) + 1)], XAC, VAC], fmt='%1.8E')
outputName='VAC'+inputfile+'unzoomed'+str(unzoomedFactor)
np.savetxt(outputName, np.c_[[t*newdt for t in range(len(VAC))], VAC, VACvariance/np.sqrt(numberOfTraj)], fmt='%1.8E')

outputName='XAC'+inputfile+'unzoomed'+str(unzoomedFactor)
np.savetxt(outputName, np.c_[[t*newdt for t in range(len(XAC))], XAC, XACvariance/np.sqrt(numberOfTraj)], fmt='%1.8E')
#np.savetxt(outputName, np.c_[XAC, VAC], fmt='%1.8E')
print(inputfile+'unzoomed'+str(unzoomedFactor))
#print(np.mean([[2,2], [1,1]], axis=0))





