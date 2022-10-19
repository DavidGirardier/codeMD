import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

sigma = 10.74
epsilon = 0.049
rcut = 26.5
r = 0.0
invr = 0.0
distance = 12.0

def EnergyLJ(distance):
  inverseDistance= 1.0/distance
  E = 0.0
  if distance < rcut :
    E = 4*epsilon*(sigma**12.0*inverseDistance**12.0 - sigma**6.0*inverseDistance**6.0)
  else : 
    E = 0.0
  return E

def minusEnergyLJ(distance):
  inverseDistance= 1.0/distance
  E = 0.0
  if distance < rcut :
    E = -4*epsilon*(sigma**12.0*inverseDistance**12.0 - sigma**6.0*inverseDistance**6.0)
  else : 
    E = 0.0
  return E

def ForceLJ(distance) :
  inverseDistance= 1.0/distance
  F = 0.0
  F = 24*epsilon*inverseDistance*(2.0*sigma**12.0*inverseDistance**12.0- sigma**6.0*inverseDistance**6.0)
  return F

def derivativeForceLJ(distance) :
  inverseDistance= 1.0/distance
  DF = 0.0
  DF = 24.0*epsilon*inverseDistance**2.0*(-26.0*sigma**12.0*inverseDistance**12.0 + 7.0*sigma**6.0*inverseDistance**6.0)
  return DF

def secondDerivativeForceLJ(distance) :
  inverseDistance= 1.0/distance
  DDF = 0.0
  DDF = 24.0*epsilon*inverseDistance**3.0*(364.0*sigma**12.0*inverseDistance**12.0 - 56.0*sigma**6.0*inverseDistance**6.0)
  return DDF

x = distance
F = ForceLJ(x)
DF = derivativeForceLJ(x)
DDF = secondDerivativeForceLJ(x)
E = EnergyLJ(12.0)
print(E)
xmin = optimize.minimize(minusEnergyLJ,20)

print(xmin)
# print(ForceLJ(14.672017))
# print(secondDerivativeForceLJ(14.672017))
# quit()
#print((-2.0*F/DDF)**0.5)
# while  abs(F) > 10**(-8):
#   x = x - F/DF
#   F = ForceLJ(x)
#   print(x)
# delta = 0.0

### Second Order Newton-Raphson ###

# while  abs(F) > 10**(-8):
#   delta = 0.0001*(-2.0*F/DDF)**0.5
#   x = x - delta
#   F = ForceLJ(x)
#   #DDF = secondDerivativeForceLJ(x)
#   print(x)



# while  abs(F) > 10**(-8):
#   x = x - F/(ForceLJ(x + 0.1) - F)
#   F = ForceLJ(x)
#   print(x)
# while  abs(F) > 10**(-8):
#   # x = x - F/DF*(1 + 1/2*F/(DF*DF)*DDF)
#   x = x - F/DF - 1/2*DF/DDF
#   F = ForceLJ(x)
#   DF = derivativeForceLJ(x)
#   DDF = secondDerivativeForceLJ(x)
#   print(x)

# while  abs(F) > 10**(-8):
#   # x = x - F/DF*(1 + 1/2*F/(DF*DF)*DDF)
#   x = x - (F/DDF)
#   F = ForceLJ(x)
#   DF = derivativeForceLJ(x)
#   #DDF = secondDerivativeForceLJ(x)
#   print(x)

### SECANT ###

# xn = distance
# Fn = ForceLJ(xn)
# while  abs(F) > 10**(-8):
#   # x = x - F/DF*(1 + 1/2*F/(DF*DF)*DDF)
#   xnp1 = xn - (Fn/DDF)
#   F = ForceLJ(x)
#   DF = derivativeForceLJ(x)
#   #DDF = secondDerivativeForceLJ(x)
#   print(x)

print(x)

# xvariables = np.arange(13.0, 17.0, 0.1)


# plt.figure()
# plt.subplot(211)
# plt.plot(xvariables, ForceLJ(xvariables), 'k', color='violet')
# plt.plot(xvariables, derivativeForceLJ(xvariables), 'k', color='r')
# plt.plot(xvariables, secondDerivativeForceLJ(xvariables), 'k', color='g')
# plt.axhline(y=0.0, color='black', linestyle='--')

# plt.show()