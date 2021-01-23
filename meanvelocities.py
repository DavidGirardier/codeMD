import numpy as np


##Read File

file = open('trajectories.out', 'r')
Lines = file.readlines()
velocities=[]
counter = 0
sumvelocities = 0.0
meanforce = 0.0
for line in Lines:

    if not(line[0]=='#'):
        counter = counter + 1
        splitted = line.split()
        splitted = [float(i) for i in splitted] #split each line
        sumvelocities = sumvelocities + (splitted[3]**2 + splitted[4]**2 + splitted[5]**2)**(0.5)
        velocities.append(splitted[:]) #Make a matrix made of each positions

meanvelocities = sumvelocities/counter

print(counter)
print(meanvelocities)
