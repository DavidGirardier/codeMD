import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, ifftshift
import glob
from pathCV import s


inputfile= 'ntraj10000_Z1g1.0m1.0'


files= glob.glob(inputfile+'*')
unzoomedFactor = 1
dt = 0.001
#print(files)



for f in files:
    print(str(f))
    Twodim = np.array(np.loadtxt(f))
    x_ref_range = (-2,2)
    npointsref = 21
    lamb = 1./((x_ref_range[1]-x_ref_range[0])/(npointsref-1))
    x_ref = np.linspace(x_ref_range[0], x_ref_range[1], npointsref)
    #y_ref = np.zeros(npointsref)
    y_ref = x_ref*0.
    #y_ref = x_ref*x_ref*x_ref

    references = [np.array([x_ref[i],y_ref[i]]) for i in range(npointsref)]
    pathcv = []
    for t in range(len(Twodim[:,0])):
        pathcv.append(s(np.array([Twodim[t,1],Twodim[t,2]]),references,lamb))
    outputName = 'pathCVlong_'+f    
    np.savetxt(outputName, np.c_[Twodim[:,0], pathcv], fmt='%1.8E')