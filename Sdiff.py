from numpy import sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz, transpose, float128

def correlation_FFT(x1, x2, norm=True, mean=False):
    #computing the lenght of the vectors
    n1 = len(x1)
    n2 = len(x2)
    #checking if the vectors has the same lenght (MANDATORY)
    if (n1!=n2):
        print('different lenght vectors!')
        exit()
    #rename the variable
    n = n1
    #statistical analysis on data
    var1 = x1.var()
    var2 = x2.var()
    xx1 = x1
    xx2 = x2
    #print('working')
    if mean==True:
        xx1 = x1 - x1.mean()
        xx2 = x2 - x2.mean()
    #computing correlation
    result = correlate(xx1, xx2, mode="full")[-n:]
    result /= arange(n, 0, -1)
    #normalizing the correlation function
    norm1 = sqrt(var1)
    norm2 = sqrt(var2)
    if norm:
        result /= (norm1*norm2)
        return result
    else:
        return result


#Input
norm = False
mmean = False
every = 20.

dt = (41.341/4.0)*every
freq = 1.0

species = 'Cl'
N = 108



file = open('collected_vneg80000.txt', 'r')
Lines = file.readlines()
counter = -1
conversion=((1.8897261254535*0.317)/(41.341374575751 * 7.026280076))
vx=[]
vy=[]
vz=[]
countime = 0
for line in Lines:
    #print('reading')
    if not(line[0]=='#'):
        counter = counter + 1
        if (((counter+1)%216)==0):
            countime = countime + 1




        if (((countime)%every)==0):
            splitted = line.split()
            splitted = [float(i) for i in splitted] #split each line
            vx.append(splitted[0]*conversion)
            vy.append(splitted[1]*conversion)
            vz.append(splitted[2]*conversion)

        # if ((counter+1)==(216*200000)):
        #     break





vx = array(vx)
vy = array(vy)
vz = array(vz)



#vcmx, vcmy, vcmz = loadtxt("../Analysis.txt", usecols=(7,8,9), unpack=True)

if (len(vx)%N==0):
  Nt = len(vx)//N
  t = arange(Nt)*dt*freq

else:
  raise TypeError('Dimension of velocities is not an integer multiple of the number of particles')
vx, vy, vz = array(split(vx, Nt)), array(split(vy, Nt)), array(split(vz, Nt))
vx, vy, vz = swapaxes(vx, 0, 1), swapaxes(vy, 0, 1), swapaxes(vz, 0, 1)
VCTxx = array([correlation_FFT(vx[i], vx[i], norm=norm, mean=mmean) for i in range(N)])
VCTyy = array([correlation_FFT(vy[i], vy[i], norm=norm, mean=mmean) for i in range(N)])
VCTzz = array([correlation_FFT(vz[i], vz[i], norm=norm, mean=mmean) for i in range(N)])
VCTxy = array([correlation_FFT(vx[i], vy[i], norm=norm, mean=mmean) for i in range(N)])
VCTxz = array([correlation_FFT(vx[i], vz[i], norm=norm, mean=mmean) for i in range(N)])
VCTyx = array([correlation_FFT(vy[i], vx[i], norm=norm, mean=mmean) for i in range(N)])
VCTyz = array([correlation_FFT(vy[i], vz[i], norm=norm, mean=mmean) for i in range(N)])
VCTzx = array([correlation_FFT(vz[i], vx[i], norm=norm, mean=mmean) for i in range(N)])
VCTzy = array([correlation_FFT(vz[i], vy[i], norm=norm, mean=mmean) for i in range(N)])
VCT = array([[VCTxx, VCTxy, VCTxz], [VCTyx, VCTyy, VCTyz], [VCTzx, VCTzy, VCTzz]])

VCTxx = mean(VCTxx, axis=0)
VCTyy = mean(VCTyy, axis=0)
VCTzz = mean(VCTzz, axis=0)
VCTxy = mean(VCTxy, axis=0)
VCTyx = mean(VCTyx, axis=0)
VCTxz = mean(VCTxz, axis=0)
VCTyz = mean(VCTyz, axis=0)
VCTzx = mean(VCTzx, axis=0)
VCTzy = mean(VCTzy, axis=0)

if mmean == True :
  if norm == True :
      savefile = 'vacf_mean_norm_'+species+'.out'
  else:
      savefile = 'vacf_mean_nonorm_'+species+'.out'

if mmean == False :
  if norm == True :
      savefile = 'vacf_nomean_norm_'+species+'.out'
  else:
      savefile = 'vacf_nomean_nonorm_'+species+'.out'

savetxt(savefile, c_[t, VCTxx, VCTyy, VCTzz, VCTxy, VCTxz, VCTyx, VCTyz, VCTzx, VCTzy])
#savetxt(savefile, c_[t, VCTxy, VCTyx, VCTxz, VCTzx,])
file.close()




# species = 'Na'
# N = 108
#
#
#
#
#
# #vx, vy, vz = loadtxt('trajectories.out',comments='#', usecols=(3,4,5), unpack=True)
# file = open('collected_vpos80000.txt', 'r')
# Lines = file.readlines()
# counter = -1
# conversion=((1.8897261254535*0.317)/(41.341374575751 * 7.026280076))
# vx=[]
# vy=[]
# vz=[]
# countime = 0
# for line in Lines:
#     #print('reading')
#     if not(line[0]=='#'):
#         counter = counter + 1
#         if (((counter+1)%216)==0):
#             countime = countime + 1
#
#
#
#
#         if (((countime)%every)==0):
#             splitted = line.split()
#             splitted = [float(i) for i in splitted] #split each line
#             vx.append(splitted[0]*conversion)
#             vy.append(splitted[1]*conversion)
#             vz.append(splitted[2]*conversion)
#
#
#         # if ((counter+1)==(216*200000)):
#         #     break
#
#
#
# vx = array(vx)
# vy = array(vy)
# vz = array(vz)
# if (len(vx)%N==0):
#   Nt = len(vx)//N
#   t = arange(Nt)*dt*freq
# else:
#   raise TypeError('Dimension of velocities is not an integer multiple of the number of particles')
# vx, vy, vz = array(split(vx, Nt)), array(split(vy, Nt)), array(split(vz, Nt))
# vx, vy, vz = swapaxes(vx, 0, 1), swapaxes(vy, 0, 1), swapaxes(vz, 0, 1)
# VCTxx = array([correlation_FFT(vx[i], vx[i], norm=norm, mean=mmean) for i in range(N)])
# VCTyy = array([correlation_FFT(vy[i], vy[i], norm=norm, mean=mmean) for i in range(N)])
# VCTzz = array([correlation_FFT(vz[i], vz[i], norm=norm, mean=mmean) for i in range(N)])
# VCTxy = array([correlation_FFT(vx[i], vy[i], norm=norm, mean=mmean) for i in range(N)])
# VCTxz = array([correlation_FFT(vx[i], vz[i], norm=norm, mean=mmean) for i in range(N)])
# VCTyx = array([correlation_FFT(vy[i], vx[i], norm=norm, mean=mmean) for i in range(N)])
# VCTyz = array([correlation_FFT(vy[i], vz[i], norm=norm, mean=mmean) for i in range(N)])
# VCTzx = array([correlation_FFT(vz[i], vx[i], norm=norm, mean=mmean) for i in range(N)])
# VCTzy = array([correlation_FFT(vz[i], vy[i], norm=norm, mean=mmean) for i in range(N)])
# VCT = array([[VCTxx, VCTxy, VCTxz], [VCTyx, VCTyy, VCTyz], [VCTzx, VCTzy, VCTzz]])
#
# VCTxx = mean(VCTxx, axis=0)
# VCTyy = mean(VCTyy, axis=0)
# VCTzz = mean(VCTzz, axis=0)
# VCTxy = mean(VCTxy, axis=0)
# VCTyx = mean(VCTyx, axis=0)
# VCTxz = mean(VCTxz, axis=0)
# VCTyz = mean(VCTyz, axis=0)
# VCTzx = mean(VCTzx, axis=0)
# VCTzy = mean(VCTzy, axis=0)
#
# if mmean == True :
#     if norm == True :
#         savefile = 'vacf_mean_norm_'+species+'.out'
#     else:
#         savefile = 'vacf_mean_nonorm_'+species+'.out'
#
# if mmean == False :
#     if norm == True :
#         savefile = 'vacf_nomean_norm_'+species+'.out'
#     else:
#         savefile = 'vacf_nomean_nonorm_'+species+'.out'
#
# savetxt(savefile, c_[t, VCTxx, VCTyy, VCTzz, VCTxy, VCTxz, VCTyx, VCTyz, VCTzx, VCTzy])
# # savetxt(savefile, c_[t, VCTxy, VCTyx, VCTxz, VCTzx,])
