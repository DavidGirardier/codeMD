import numpy as np
import matplotlib.pyplot as plt
# Generate a random signal
trajectory = np.loadtxt('COLVAR10nsAlldt')
signal = trajectory[:,1]

# Compute the autocorrelation using FFT
fft_signal = np.fft.fft(signal)
power_spectrum = np.abs(fft_signal)**2
autocorr = np.fft.ifft(power_spectrum)
autocorr = np.real(autocorr)


# Normalize the autocorrelation
norm_autocorr = autocorr / autocorr[0]

# Plot the normalized autocorrelation
plt.plot(norm_autocorr)
plt.xlabel('Lag')
plt.ylabel('Normalized Autocorrelation')
plt.show()