import numpy as np
a=2
b=0.5
N=1000
multi = 1.0
for k in range(N):
    multi = multi * (a + 2.0*b * np.cos(k*np.pi/(N+1) ))

