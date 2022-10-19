import numpy as np
import math 
import matplotlib.pyplot as plt
import time

def MeritFunction(x) : 
    MeritFunction = 1./2.*F(x)*F(x)
    return MeritFunction

def F(x) :
    F = abs(x)**(1./3.)*np.sign(x)
    # if x < 0:
    #     x = abs(x)
    #     F = x**(1/3)*(-1)
    # else :
    #     F = x**(1/3)
    #F = x**2
    #F = -x**5. + x**3. + 4.*x
    return F

def f(x) :
    f = 1./3.*abs(x)**(-2./3.)
    #f = 2*x
    #f = -5.*x**4. + 3*x**2. + 4.
    return f
def tangent(x,xn) :
    tangent = f(xn)*x + (F(xn) - f(xn)*xn)
    return tangent
def tangentMerit(x,xn,c1) :
    tangent = c1*F(xn)*f(xn)*x + (0.5*F(xn)*F(xn) - c1*F(xn)*f(xn)*xn)
    return tangent
# plt.plot(x_tot,F(x_tot))
# plt.axhline(y=0.0, color='black', linestyle='--')
# plt.plot(x_tot,MeritFunction(x_tot), color='blue')
# plt.pause(5.0)
# plt.plot(x0,F(x0), marker="o")
# plt.pause(2)
# plt.plot(x0,MeritFunction(x0), marker="o")
# plt.plot(x_tot,tangentMerit(x_tot,x0), linestyle='--')
# plt.pause(2)
# plt.plot(x_tot,tangent(x_tot,x0))

# plt.pause(1)
# x1 = x0 - alpha*F(x0)/f(x0)
# plt.plot(x1,MeritFunction(x1), marker="o")
# plt.pause(5)

# alpha = alpha*0.5
# x1 = x0 - alpha*F(x0)/f(x0)
# plt.plot(x1,MeritFunction(x1), marker="o")
# plt.pause(5)

# alpha = alpha*0.5
# x1 = x0 - alpha*F(x0)/f(x0)
# plt.plot(x1,MeritFunction(x1), marker="o")
# plt.pause(5)



alphaInitial = 1.0
alpha = alphaInitial
c1 = 0.5
x_tot = np.arange(-1,1,0.01)
xold = 1.0
count = 0
xnew = 0.0
plt.plot(x_tot,F(x_tot))
plt.axhline(y=0.0, color='black', linestyle='--')
plt.plot(x_tot,MeritFunction(x_tot), color='blue')
plt.ylim(-1, 2)

while  (abs(F(xold)) > 10**(-8) and count<10):
    plt.plot(xold,F(xold), marker="o")
    plt.pause(1)
    #plt.plot(xold,MeritFunction(xold), marker="o")
    # plt.plot(x_tot,tangentMerit(x_tot,xold), linestyle='--')
    plt.plot(x_tot,tangent(x_tot,xold))
    plt.pause(1)
    xnew = xold - alpha*F(xold)/f(xold)
    if (MeritFunction(xnew) > tangentMerit(xnew,xold,c1)):
        while ((MeritFunction(xnew) > tangentMerit(xnew,xold,c1))) :
            alpha = alpha*0.5
            xnew = xold - alpha*F(xold)/f(xold)

    count = count + 1
    xold = xnew
    alpha = alphaInitial
    print(xnew)
    # delta = 0.0
plt.show()