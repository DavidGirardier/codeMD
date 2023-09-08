import numpy as np
def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

inputfile = 'VACzeta10ns_modifunzoomed1'

VAC=np.loadtxt(inputfile)

space = 10
movedMean = running_mean(VAC[:,1],space)



