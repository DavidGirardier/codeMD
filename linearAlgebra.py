import numpy as np

#matrix = np.loadtxt('matrix.txt')
matrix = np.array([[0., 0.], [0., 0.]])

det = np.linalg.det(matrix)
invmatrix = np.linalg.inv(matrix)
#print("det = " + str(det) + " \n")

print(invmatrix[:][:])
