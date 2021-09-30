import numpy as np


##Read File

file = open('temperature.out', 'r')
Lines = file.readlines()
temperature=[]
counter = 0
sumTemperature = 0.0
meanTemperature = 0.0
for line in Lines:

    if not(line[0]=='#'):
        counter = counter + 1
        splitted = line.split()
        splitted = [float(i) for i in splitted] #split each line
        sumTemperature += splitted[1]
        temperature.append(splitted[:]) #Make a matrix made of each positions

meanTemperature = sumTemperature/counter

print(counter)
print(meanTemperature)
