from numpy import sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz, transpose, float128

inputfile = input("Diff file: ")
file = open(inputfile, 'r')


fileLines = file.readlines()

meanDiffxxyy = 0
meanDiffzz = 0
meanDiffxy = 0
meanDiffyx = 0
meanDiffxz = 0


count= 0
for line in fileLines:
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted]
    if (splitted[0]/(41.341*1000) > 0.5) and (splitted[0]/(41.341*1000) < 1.):
        #print(splitted[0])
        count = count + 1

        meanDiffxxyy += (0.5*(splitted[1]+splitted[2])*1.15)
        meanDiffzz += (splitted[3]*1.15)
        meanDiffxy += (splitted[4]*1.15)
        meanDiffyx += (splitted[6]*1.15)
        meanDiffxz += (splitted[5]*1.15)


print(meanDiffxy)


print("meanDiffxxyy = " + str(meanDiffxxyy/count) + "\n meanDiffzz = " + str(meanDiffzz/count) + "\n meanDiffxy = " + str(meanDiffxy/count) + "\n meanDiffyx = " + str(meanDiffyx/count)  + "\n meanDiffxz = " + str(meanDiffxz/count))
