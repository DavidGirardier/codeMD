import numpy as np
import os

import matplotlib.pyplot as plt


step = 50
N = 120000
# Process files in groups of 10
group_size = 200
for i in range(0, N, group_size*step):
    # Get the current group of 10 files
    list_clusters = np.empty(0)
    list_gr = np.empty(0)
    print(i)
    for j in range(i, i+group_size*step, step):
        name_file = 'cs.'+str(j)
        cs = np.loadtxt(name_file)
        #print(cs[:,1])
        list_clusters = np.concatenate((list_clusters.ravel(),cs[:,1].ravel()))
        list_gr = np.concatenate((list_clusters.ravel(),cs[:,5].ravel()))
        
        
    


    list_clusters = list_clusters[list_clusters != 1]
    max_cs = int(np.max(list_clusters))
    frequencies, bin_edges = np.histogram(list_clusters, bins=int(max_cs/2))
    hist_data = np.column_stack((bin_edges[:-1], frequencies))
    np.savetxt('histogram_cs'+str(i)+'.txt', hist_data, fmt='%f', header='Bin Edges   Frequencies')
    
    
    frequencies, bin_edges = np.histogram(list_gr, bins=100)

    hist_data = np.column_stack((bin_edges[:-1], frequencies))

    np.savetxt('histogram_gr'+str(i)+'.txt', hist_data, fmt='%f', header='Bin Edges   Frequencies')

    print("Histogram data saved to 'histogram_data.txt'.")
    # print(list_clusters)
    # exit()

