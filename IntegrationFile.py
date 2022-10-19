import numpy as np

matrix = np.loadtxt('../Multimaze/results/WithCellList/GofR_SmallSmall.txt')

matrixSize = len(matrix)

integral = 0.0

for i in range(1,matrixSize):
    differenceX = (matrix[i][0]- matrix[i-1][0])
    meanY = (matrix[i][1]+ matrix[i-1][1])/2
    integral = integral + differenceX*meanY

print(integral)