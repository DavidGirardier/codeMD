import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment


inputfile = 'ProfFinalOpti5Loop_fraction500traj2ps_newdt0_1'


fractions = 5
x = []
y = []
z = []
FEs = []
gammas = []
for i in range(1,fractions+1):
    inputfilefrac = inputfile+'_'+str(i)

    profile = np.loadtxt(inputfilefrac)
    #print(min(profile[:500,1]))
    FEs.append(profile[:,1])
    FEs.append(profile[:,1]- min(profile[:200,1]))
    gammas.append(profile[:,3])
FEs = np.array(FEs)
gammas = np.array(gammas)
q = profile[:,0]



FE_mean_curve = np.mean(FEs, axis=0)
FE_std_curve = np.std(FEs, axis=0)
gamma_mean_curve = np.mean(gammas, axis=0)
gamma_std_curve = np.std(gammas, axis=0)

outputName = 'MeanAndVarFE'+'_'+inputfile
print(outputName)
#print(outputName)
np.savetxt(outputName, np.c_[q,FE_mean_curve,FE_std_curve/fractions], fmt='%1.8E')
outputName = 'MeanAndVarGamma'+'_'+inputfile
np.savetxt(outputName, np.c_[q,gamma_mean_curve,gamma_std_curve/fractions], fmt='%1.8E')
#np.savetxt(outputName, np.c_[q,], fmt='%1.8E')



# Calculate pairwise distances between curves using Euclidean distance
distances = cdist(FEs, FEs, metric='euclidean')

# Use the Hungarian algorithm to find the optimal assignment
row_ind, col_ind = linear_sum_assignment(distances)

# Reorder the curves based on the optimal assignment
aligned_curves = FEs[row_ind]

mean_curve = np.mean(aligned_curves, axis=0)

# Compute the variance of the aligned curves
variance_curve = np.var(aligned_curves, axis=0)

# Plot the curves
for curve in aligned_curves:
    plt.plot(q,curve, alpha=0.4, color='gray', linewidth=1)

# Plot the mean curve
plt.plot(q,mean_curve, color='blue', linewidth=2, label='Mean Curve')

# Plot the variance curve
plt.plot(q,mean_curve + variance_curve, color='red', linestyle='--', linewidth=1, label='Mean + Variance')
plt.plot(q,mean_curve - variance_curve, color='red', linestyle='--', linewidth=1, label='Mean - Variance')
plt.fill_between(q, mean_curve - variance_curve, mean_curve + variance_curve, color='red', alpha=0.2)

# Set plot labels and legend
plt.xlabel('q')
plt.ylabel('kT')
plt.legend()

# Display the plot
plt.show()