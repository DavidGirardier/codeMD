import numpy as np


##Read File

file = open('forces.out', 'r')
Lines = file.readlines()
forces=[]
counter = 0
intermolecular_forces = 0.0
lorentz_forces = 0.0
mean_intermolecular = 0.0
mean_lorentz = 0.0
ratio = 0.0
for line in Lines:

    if not(line[0]=='#'):
        counter = counter + 1
        splitted = line.split()
        splitted = [float(i) for i in splitted] #split each line
        intermolecular_forces = intermolecular_forces + (splitted[0]**2 + splitted[1]**2 + splitted[2]**2)**(0.5)
        lorentz_forces = lorentz_forces + (splitted[12]**2 + splitted[13]**2 + splitted[14]**2)**(0.5)


mean_intermolecular = intermolecular_forces/counter
mean_lorentz = lorentz_forces/counter
ratio = mean_lorentz / (mean_lorentz + mean_intermolecular)
print("Mean Intermolecular forces = " + str(mean_intermolecular) +"\n")
print("Mean Lorentz forces = " + str(mean_lorentz) +"\n")
print("Ratio Lorentz = " + str(ratio) + "\n")
