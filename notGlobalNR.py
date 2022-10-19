import numpy as np
import math 
import matplotlib.pyplot as plt
import time


def F(x) :
    #F = abs(x)**(1./3.)*np.sign(x)
    # if x < 0:
    #     x = abs(x)
    #     F = x**(1/3)*(-1)
    # else :
    #     F = x**(1/3)
    #F = x**2
    F = -x**5. + x**3. + 4.*x
    return F

def f(x) :
    #3f = 1./3.*abs(x)**(-2./3.)
    #f = 2*x
    f = -5.*x**4. + 3*x**2. + 4.
    return f
def tangent(x,xn) :
    tangent = f(xn)*x + (F(xn) - f(xn)*xn)
    return tangent
alpha = 1.0
x_tot = np.arange(-2,2,0.01)
x0 = 1.0

plt.plot(x_tot,F(x_tot))
plt.axhline(y=0.0, color='black', linestyle='--')
plt.pause(1.0)
plt.plot(x0,F(x0), marker="o")
plt.pause(0.5)
plt.plot(x_tot,tangent(x_tot,x0))

plt.pause(1)
x1 = x0 - alpha*F(x0)/f(x0)
plt.plot(x1,F(x1), marker="o")
plt.pause(0.5)
plt.plot(x_tot,tangent(x_tot,x1))
plt.pause(1)
x2 = x1 - alpha*F(x1)/f(x1)
plt.plot(x2,F(x2), marker="o")
plt.pause(0.5)
plt.plot(x_tot,tangent(x_tot,x2))
plt.pause(1)
plt.show()
# x = 1.
# count = 0
# exit()
# while  (abs(F(x)) > 10**(-8) or count>1e3):
#     x = x - alpha*F(x)/f(x)
#     count = count + 1
#     print(x)
#     delta = 0.0