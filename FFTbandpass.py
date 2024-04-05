import numpy as np
from scipy.fft import rfft, irfft, rfftfreq, fft, ifft, fftfreq, dct, idct
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt


plot_option=False
threshold_freq = 25
inputfile = input('Trajectory File:')
trajectories = np.loadtxt(inputfile)
# trajectories = np.loadtxt(inputfile)

# time = np.linspace(0,1,100000)
# pos = np.exp(-3*time) + 0.1*np.cos(300*time)

time = trajectories[:,0] 
pos = trajectories[:,1]
d=time[1]-time[0]
W = fftfreq(time.size, d=time[1]-time[0])
f_signal = dct(pos,type=1)


# If our original signal time was in seconds, this is now in Hz    
cut_f_signal = f_signal.copy()
cut_f_signal[(abs(W)>threshold_freq)] = 0

cut_signal = idct(cut_f_signal,type=1)

if plot_option == True:
    

    plt.subplot(2, 2, 1)
    plt.plot(time, pos, label='CV')
    plt.xlabel('t [ps]')
    # plt.ylabel('Cv(t)')
    plt.legend()

    plt.subplot(2, 2, 2)

    plt.plot(W,np.abs(f_signal), label='F-space')
    plt.xlabel('w [ps-1]')
    # plt.ylabel('Cv(t)')
    plt.legend()

    plt.subplot(2, 2, 4)

    plt.plot(W,np.abs(cut_f_signal), label='F-space filtered')

    plt.xlabel('w [ps-1]')
    # plt.ylabel('Cv(t)')
    plt.legend()

    plt.subplot(2, 2, 3)

    plt.plot(time,cut_signal, label='CV filtered')

    plt.xlabel('t [ps]')
    # plt.ylabel('Cv(t)')
    plt.legend()

    plt.show()

    # plt.plot(time,pos)

    # plt.plot(W,f_signal)

    # plt.subplot(223)
    # plt.plot(W,cut_f_signal)

    # plt.subplot(224)
    # plt.plot(time,cut_signal)
    # plt.show()

    period = 0.2
    pos_savgol = savgol_filter(pos, int(period/d), 5)

    plt.subplot(2, 1, 1)
    plt.plot(time, pos, label='CV')
    plt.xlabel('t [ps]')
    # plt.ylabel('Cv(t)')
    plt.legend()

    plt.subplot(2, 1, 2)

    plt.plot(time,pos_savgol, label='Savgol')
    plt.xlabel('w [ps-1]')
    # plt.ylabel('Cv(t)')
    plt.legend()
    plt.show()


outputName='filtered_'+inputfile
np.savetxt(outputName, np.c_[time, cut_signal], fmt='%1.8E')
