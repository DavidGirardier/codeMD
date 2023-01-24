import numpy as np



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


inputfile = 'colvar_d_c240'
trajectories = np.loadtxt(inputfile, max_rows=3)

unzoomedFactor = 1

dt = trajectories[1,0]
numberOfTraj = 100
tFile = 100.0
nLine = tFile/dt
newdt = dt * unzoomedFactor

matrixXAC = []

for i in range(numberOfTraj):
    trajectory = np.loadtxt(inputfile, skiprows=int(nLine)*i, max_rows=int(nLine)+1)
    unzoomedPos = [x for x in trajectory]
    
    matrixXAC.append(autocorrelation(trajectory[::unzoomedFactor,0]))
    
    trajectory = []

outputName='XACunzoomed' + str(unzoomedFactor)
XAC = np.mean(matrixXAC, axis=0)
np.savetxt(outputName, np.c_[[t*newdt for t in range(int(tFile/newdt) + 1)], XAC], fmt='%1.8E')

#print(np.mean([[2,2], [1,1]], axis=0))




