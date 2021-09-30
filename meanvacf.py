from numpy import sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz


##Read File
inputfile = input("Vacf file: ")
file = open(inputfile, 'r')
Lines = file.readlines()
mean = 0.0
dt=[]
meanVacf=[]
counter = -1
for line in Lines:

    if not(line[0]=='#'):
        counter+=1
        splitted = line.split()
        splitted = [float(i) for i in splitted] #split each line
        mean = (splitted[1] + splitted[2] + splitted[3])/3
        meanVacf.append(mean)
        dt.append(counter/1000)
    if counter==999:
        break

outputfile = 'mean_' + inputfile
savetxt(outputfile, c_[dt,meanVacf])#,Dxy])
