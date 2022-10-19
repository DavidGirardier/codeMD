import matplotlib.pyplot as plt
import numpy as np
import os

if os.path.exists("wrappedCheckpoint.txt"):
    os.remove("wrappedCheckpoint.txt")

inputfile = "checkpoint.txt"

file = open(inputfile, 'r')
Lines = file.readlines()
counter = -1
splitted = Lines[0].split()
splitted = [float(i) for i in splitted]
N = int(splitted[0])
boxLenght = splitted[1]
headerLine = str(N) + '\t' + str(boxLenght)
shufflingList = []

with open('wrappedCheckpoint.txt', 'a') as the_file:
    the_file.write(str(headerLine)+'\n')

    for k in range(1,N+1):
        splitted = Lines[k].split()
        splitted = [float(i) for i in splitted]

        x = splitted[0] - boxLenght*round(splitted[0]/boxLenght)
        y = splitted[1] - boxLenght*round(splitted[1]/boxLenght)
        z = splitted[2] - boxLenght*round(splitted[2]/boxLenght)

        xtm1 = splitted[6] - boxLenght*round(splitted[0]/boxLenght)
        ytm1 = splitted[7] - boxLenght*round(splitted[1]/boxLenght)
        ztm1 = splitted[8] - boxLenght*round(splitted[2]/boxLenght)

        vx = splitted[9]
        vy = splitted[10]
        vz = splitted[11]

        the_file.write(str(x)+' '+str(y)+' '+str(z)+' '+str(x)+' '+str(y)+' '+str(z)+' '+str(xtm1)+' '+str(ytm1)+' '+str(ztm1)+' '+str(vx)+' '+str(vy)+' '+str(vz)+' '+str(vx)+' '+str(vy)+' '+str(vz)+' '+'\n')
