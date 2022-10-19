from heapq import nsmallest
import numpy as np

SmallNumber = 6
TimeStepsNumber = 318
SmallConfiguration1 = np.loadtxt("8partCG1fs/PSconfig/r_neg_t.txt")
SmallConfiguration2 = np.loadtxt("8partMaZets1fsExplo/PSconfig/r_neg_t.txt")
sumAbs = 0
DistanceSmallConf = []
for i in range(TimeStepsNumber):
    sumAbs = 0
    for j in range(SmallNumber):
        sumAbs = sumAbs + ((SmallConfiguration1[SmallNumber*i + j][0] - SmallConfiguration2[SmallNumber*i + j][0])**2.0 + (SmallConfiguration1[SmallNumber*i + j][1] - SmallConfiguration2[SmallNumber*i + j][1])**2.0 + (SmallConfiguration1[SmallNumber*i + j][2] - SmallConfiguration2[SmallNumber*i + j][2])**2.0)**(0.5)
    DistanceSmallConf.append(sumAbs)
np.savetxt('distanceSmall.txt',DistanceSmallConf)

BigNumber = 2
TimeStepsNumber = 318
BigConfiguration1 = np.loadtxt("8partCG1fs/PSconfig/r_pos_t.txt")
BigConfiguration2 = np.loadtxt("8partMaZets1fsExplo/PSconfig/r_pos_t.txt")
sumAbs = 0
DistanceBigConf = []
for i in range(TimeStepsNumber):
    sumAbs = 0
    for j in range(BigNumber):
        sumAbs = sumAbs + ((BigConfiguration1[BigNumber*i + j][0] - BigConfiguration2[BigNumber*i + j][0])**2.0 + (BigConfiguration1[BigNumber*i + j][1] - BigConfiguration2[BigNumber*i + j][1])**2.0 + (BigConfiguration1[BigNumber*i + j][2] - BigConfiguration2[BigNumber*i + j][2])**2.0)**(0.5)
    DistanceBigConf.append(sumAbs)
np.savetxt('distanceBig.txt',DistanceBigConf)

print(((SmallConfiguration1[10][0] - SmallConfiguration2[10][0])**2.0 + (SmallConfiguration1[10][1] - SmallConfiguration2[10][1])**2.0 + (SmallConfiguration1[10][2] - SmallConfiguration2[10][2])**2.0)**(0.5))