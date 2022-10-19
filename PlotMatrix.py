import numpy as np
import matplotlib.pyplot as plt

matrix = np.loadtxt('../Multimaze/BmatrixCellListd0_0127rc11.txt')

meanNonZeroPerLine = np.count_nonzero(matrix[0][:])

print(meanNonZeroPerLine)
exit
plt.imshow(matrix)
plt.colorbar()
plt.show()

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True

# fig, ax = plt.subplots()
# min_val, max_val = 0, 5
# matrix = np.random.randint(0, 5, size=(max_val, max_val))
# ax.matshow(matrix, cmap='ocean')

# for i in range(max_val):
#    for j in range(max_val):
#       c = matrix[j, i]
#       ax.text(i, j, str(c), va='center', ha='center')

# plt.show()
