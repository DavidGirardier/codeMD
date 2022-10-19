from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
s = 'a3b5ce'
ch : str = ''

rep : str = ''

c : str

for c in s:
    if '0' <= c <= '9':
        rep = rep + c
    else :
        if rep != '':
            print(c,'\t',rep,'\n')
            ch = ch + (c* int(rep))
            rep =''
        else:
            ch = ch + c

print(ch)