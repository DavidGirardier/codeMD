#from cmath import inf
import numpy as np
import math

#matrix = np.loadtxt('SHAKEmatrixEXPLOSION.txt')
matrix = np.loadtxt('SHAKEmatrix.txt')
b = np.loadtxt('FULLPHI.txt')
# m = matrix - matrix2
# absm = np.absolute(m)
# maxItem = 0.
# maxIndex = []
# for i in range(300):
#      for j in range(300):
#          if (absm[i][j]>maxItem):
#              maxItem = absm[i][j]
#              maxIndex = [i, j]
             

# print("index :" + str(maxIndex[0]) + "/" + str(maxIndex[1])  + " and max = " + str(maxItem))

minimumValue = 100
minIndex = []
absMatrix = np.absolute(matrix)
# for i in range(300):
#      for j in range(300):
#          if (minimumValue>absMatrix[i][j]):
#              minimumValue = absMatrix[i][j]
#              minIndex = [i, j]
# print("index of min :" + str(minIndex[0]+1) + "/" + str(minIndex[1]+1)  + " and min = " + str(minimumValue) + '\n')
# phiWithoutZeros
# for i in range(b.lenght):
#     if 

#matrix = np.array([[1., 1., 2], [2., 1., 2], [0, 0, 0]])
#print(matrix[0][299])
det = np.linalg.det(matrix)
#invmatrix = np.linalg.inv(matrix)
#print("det = " + str(det) + " \n")
#x, residuals, rank, s = np.linalg.lstsq(matrix,b,rcond=None)

#print(b-matrix@x)

# for i in range(300):
#     if (matrix[i][i] < 1e-3):
#         print("diag element " + str(i) + " = " + str(matrix[i][i]))

# for i in range(100):
#     for j in range(i,100):
#         if (np.dot(matrix[i][:],matrix[j][:])  (np.linalg.norm(matrix[i][:]) + np.linalg.norm(matrix[j][:])) ):
#             print(str(i) + " and " + str(j) + " are linearly dependant")

# lambdas, V = np.linalg.eig(matrix.T)
# print(matrix[lambdas == 0, :])
#print(matrix[:][:])
#print(invmatrix[:][:])