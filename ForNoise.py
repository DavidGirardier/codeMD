from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt

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


dt = 0.001
dx = 0.2
# name = input('noise file:')
# if name != '':
#     noise = np.loadtxt(name)
# else:
#     noise = np.loadtxt('colvar_disp_scaled_from_prop')
for number in range(1,100):
    if number < 10:
        noise = np.loadtxt('colvar_disp_scaled_from_prop_0.0'+ str(number))

    else:

        noise = np.loadtxt('colvar_disp_scaled_from_prop_0.'+ str(number))
    #noise = np.loadtxt('fort.654')
    # noise=[]
    # for i in range(100000):
    #     noise.append(np.random.normal())

    # noise2 = [x*x for x in noise]
    # print('<noise> = ' + str(np.mean(noise)))
    # print('<noise^2> - <noise>^2 = ' + str(np.mean(noise2) - np.mean(noise)*np.mean(noise)))
    # AC_G1 = autocorrelation(noise)

    # time = np.arange(0,len(AC_G1),1)
    # time = time*dt
    # np.savetxt('AutocorrelationNoise1', np.c_[time,AC_G1], fmt='%1.8E')
    # exit()
    histo_noise1 = np.histogram(noise[:,0], np.arange(-4.0,4.0,dx), density=True) 


    noise2 = [x*x for x in noise[:,0]]
    print('<noise> = ' + str(np.mean(noise[:,0])))
    print('<noise^2> - <noise>^2 = ' + str(np.mean(noise2) - np.mean(noise[:,0])*np.mean(noise[:,0])))
    #print('integral = ' + str(np.trapz(histo_noise[0]/(len(noise[:,1])*dx), dx=0.1)))

    AC_G1 = autocorrelation(noise[:,0])

    # time = np.arange(0,len(AC_G1),1)
    # time = time*dt
    # np.savetxt('AutocorrelationNoise1', np.c_[time,AC_G1], fmt='%1.8E')





    histo_noise2 = np.histogram(noise[:,1], np.arange(-4.0,4.0,dx), density=True) 

    np.savetxt('Histo_ReproducedNoise' + str(number), np.c_[histo_noise2[1][:-1],histo_noise1[0],histo_noise2[0]], fmt='%1.8E')
    noise2 = [x*x for x in noise[:,1]]
    print('<noise> = ' + str(np.mean(noise[:,1])))
    print('<noise^2> - <noise>^2 = ' + str(np.mean(noise2) - np.mean(noise[:,1])*np.mean(noise[:,1])))
    #print('integral = ' + str(np.trapz(histo_noise[0]/(len(noise[:,1])*dx), dx=0.1)))

    AC_G2 = autocorrelation(noise[:,1])

    time = np.arange(0,len(AC_G2),1)
    time = time*dt
    np.savetxt('AutocorrelationNoise' + str(number), np.c_[time,AC_G1, AC_G2], fmt='%1.8E')
    

    print(number)
