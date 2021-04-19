import numpy as np

file = open("FullAnalysis.txt","r")



fileLines = file.readlines()

sum_tot=0.0
sum_tot2=0.0
avg_tot = float(0.0)
avg_tot2 = 0.0

sum_pot=0.0
sum_pot2=0.0
avg_pot = 0.0
avg_pot2 = 0.0

sum_kin=0.0
sum_kin2=0.0
avg_kin = 0.0
avg_kin2 = 0.0

count= 0
for line in fileLines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    #print(splitted[0])
    sum_tot = sum_tot + splitted[1]
    sum_tot2 = sum_tot2 + splitted[1]**2
    sum_kin = sum_kin + splitted[2]
    sum_kin2 = sum_kin2 + splitted[2]**2
    sum_pot = sum_pot + splitted[3]
    sum_pot2 = sum_pot2 + splitted[3]**2
    #print(str(sum_tot)+ '\t')
    #print(str(sum_tot2) + '\n')


avg_tot = sum_tot/count
avg_tot2 = sum_tot2/count

DE = abs((avg_tot2 - avg_tot**2))**0.5

avg_kin = sum_kin/count
avg_kin2 = sum_kin2/count
DK = abs((avg_kin2 - avg_kin**2))**0.5
#print('\n')
avg_pot = sum_pot/count
avg_pot2 = sum_pot2/count
#print(str(sum_pot) + '  ' + str(sum_pot2))
DV = abs((avg_pot2 - avg_pot**2))**0.5


print("DE/DV = " + str(DE/DV) + "\t DE = " + str(DE) + "\t DK = " + str(DK) + "\t DV = " + str(DV))
