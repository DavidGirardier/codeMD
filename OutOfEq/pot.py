import numpy as np
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython=True)
def Z1(x,y):
    pot = 10*(x**2-1.)**2+20.*y**2
    der_x = 40.*(x**2-1.)*x
    der_y = 40.*y
    return der_x, der_y, pot
@jit(nopython=True)
def Z2(x,y):
    pot = 4.*(5.*(y**2-1.)**2+1.25*(y-0.5*x)**2)
    der_x = 4.*(-1.25*(y-0.5*x))
    der_y = 4.*(20.*(y**2-1.)*y + 2.5*(y-0.5*x))
    return der_x, der_y, pot