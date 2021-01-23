import numpy as np

totfile = open('tot.txt', 'r')
potfile = open('pot.txt', 'r')


totLines = totfile.readlines()
potLines = potfile.readlines()

sum_tot=0.0
sum_tot2=0.0
avg_tot = float(0.0)
avg_tot2 = 0.0

sum_pot=0.0
sum_pot2=0.0
avg_pot = 0.0
avg_pot2 = 0.0

count= 0
for line in totLines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    #print(splitted[0])
    sum_tot = sum_tot + splitted[0]
    sum_tot2 = sum_tot2 + splitted[0]**2
    #print(str(sum_tot)+ '\t')
    #print(str(sum_tot2) + '\n')

for line in potLines:

    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    #print(splitted[0])
    sum_pot = sum_pot + splitted[0]
    sum_pot2 = sum_pot2 + splitted[0]**2
    #print(str(sum_tot)+ '\t')
    #print(str(sum_tot2) + '\n')

#print(str(sum_tot) + '  ' + str(sum_tot2))
avg_tot = sum_tot/count
avg_tot2 = sum_tot2/count

DE = abs((avg_tot2 - avg_tot**2))**0.5
print(str(DE))
#print('\n')
avg_pot = sum_pot/count
avg_pot2 = sum_pot2/count
#print(str(sum_pot) + '  ' + str(sum_pot2))
DV = abs((avg_pot2 - avg_pot**2))**0.5


print(str(DE/DV))
