import numpy as np

correction = np.loadtxt('Correction')
dt = 0.001
G1 = [x*x for x in correction[:,0]]
G2 = [correction[i,0] *correction[i,1] for i in range(len(correction[:,0]))]
print(np.mean(G1))
print(1./6.*2.*dt)

print(np.mean(G2))
print(-1./24.*2.*dt)

# print(np.mean(correction[:,2]))
# print(np.mean(correction[:,3]))
# print(np.var(correction[:,2]))
# print(np.var(correction[:,3]))
