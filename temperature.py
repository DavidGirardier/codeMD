from numpy import sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz, transpose, float128

file = open("Analysis.txt","r")



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

runningTemp = []
t=[]
sumTemp = 0
meamTemp = 0

count= 0
for line in fileLines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    #print(splitted[0])
    t.append(splitted[0])

    sumTemp = sumTemp + splitted[5]
    #print(str(sum_tot)+ '\t')
    #print(str(sum_tot2) + '\n')
    runningTemp.append(sumTemp/count)

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


print("meanTemp = " + str(sumTemp/count))
savetxt("runningTemperature.txt", c_[t,runningTemp])
