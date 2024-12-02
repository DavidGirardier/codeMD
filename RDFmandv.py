import numpy as np
import glob

names_files = glob.glob('rdf.*')

all_files = []

for i in names_files :
    file = np.loadtxt(i,comments='#')
    all_files.append(file)

print(all_files)   
mean_rdf = np.mean(all_files,axis=0)
std_rdf = np.std(all_files,axis=0)

print(mean_rdf)
err_rdf = std_rdf/np.sqrt(len(names_files))
np.savetxt('meanAnderr_rdfC-Ca', np.c_[mean_rdf[:,0], mean_rdf[:,2], err_rdf[:,2]], fmt='%1.8E')
#np.savetxt('meanAnderr_rdfOw-Ca', np.c_[mean_rdf[:,0], mean_rdf[:,3], err_rdf[:,3]], fmt='%1.8E')
#np.savetxt('meanAnderr_rdfOw-O', np.c_[mean_rdf[:,0], mean_rdf[:,5], err_rdf[:,5]], fmt='%1.8E')
#np.savetxt('meanAnderr_rdfHw-O', np.c_[mean_rdf[:,0], mean_rdf[:,9], err_rdf[:,9]], fmt='%1.8E')
#np.savetxt('meanAnderr_rdfOw-C', np.c_[mean_rdf[:,0], mean_rdf[:,4], err_rdf[:,4]], fmt='%1.8E')
#np.savetxt('err_rdf', std_rdf/np.sqrt(len(names_files)), fmt='%1.8E')