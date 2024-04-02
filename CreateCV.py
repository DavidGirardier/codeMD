import numpy as np

colvar_name = 'bf_500tps'
colvar = np.array(np.loadtxt(colvar_name))

weights_name='opt-value-david_ordered'
weights = np.array(np.loadtxt(weights_name))

num_rows, num_cols = colvar.shape
print(weights* weights)

#cv(:,i)= (cv(:,i) - minval(cv(:,i))) / (maxval(cv(:,i)-minval(cv(:,i))))
best_cv = np.copy(colvar[:,0:2])
best_cv[:,1] = 0.0
print(best_cv)
for i in range(1,num_cols):
#for i in range(1,4):
    print(i)
    if (i == 1):
        colvar[:,i] = colvar[:,i]*(-1.0)

    min_cv = np.min(colvar[:,i])
    max_cv = np.max(colvar[:,i])

    colvar[:,i] = (colvar[:,i] - min_cv)/(max_cv-min_cv)
    best_cv[:,1] =best_cv[:,1] + (colvar[:,i]*weights[i-1])


    #best_cv[:,1] =best_cv[:,1] + (colvar[:,i]*weights[i-1])*(colvar[:,i]*weights[i-1])
    #print(weights[i-1]*weights[i-1])

best_cv=best_cv*(1.0/np.sum(weights*weights))
np.savetxt('norm_'+colvar_name, colvar, fmt='%1.8E')
np.savetxt('best_'+colvar_name, best_cv, fmt='%1.8E')
