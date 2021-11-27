import numpy as np

#matrix = np.loadtxt('matrix.txt')
# matrix = np.array([[4,1,2],[1,3,2],[2,2,1]])
#
# b = [1., 2., 1.]
#
#
# #invmatrix = np.linalg.inv(matrix)
# #first step
#x_OLD = [2., 1., 1.]
#print(xold[:])
matrix = np.loadtxt('FullShakeLj.txt')
b = np.loadtxt('FullPhiLj.txt')
x_OLD = np.zeros(len(b))

# searchDirection_OLD = b - np.matmul(matrix, x_OLD)
# residue_OLD = searchDirection_OLD
# count = 0
#
# error = b - np.matmul(matrix, x_OLD)
# errorNorm = np.linalg.norm(error)
# while (errorNorm > 1e-10):
#     count += 1
#
#     alpha_OLD = np.dot(residue_OLD, residue_OLD)/(np.matmul(np.transpose(searchDirection_OLD), np.matmul(matrix, searchDirection_OLD)))
#     x_NEW = x_OLD + alpha_OLD*searchDirection_OLD
#
#     residue_NEW = residue_OLD - alpha_OLD*(np.matmul(matrix, searchDirection_OLD))
#     beta_NEW = np.dot(residue_NEW, residue_NEW)/(np.dot(residue_OLD, residue_OLD))
#     searchDirection_NEW = residue_NEW + beta_NEW*searchDirection_OLD
#
#     residue_OLD = residue_NEW
#     searchDirection_OLD = searchDirection_NEW
#     x_OLD = x_NEW
#
#     error = b - np.matmul(matrix, x_OLD)
#     errorNorm = np.linalg.norm(error)
#
#
#     #print(x_OLD)
#     if count > 1000:
#         print("Max iteration reached")
#         break
alpha_num = 0.
alpha_denom = 0.
beta_num = 0.
beta_denom = 0.
N = len(x_OLD)
residue_OLD = np.zeros(N)
searchDirection_OLD = np.zeros(N)
residue_NEW = np.zeros(N)
searchDirection_NEW = np.zeros(N)
count = 0

error = np.zeros(N)
errorNorm = 0.

error = b - np.matmul(matrix, x_OLD)
errorNorm = np.linalg.norm(error)


for i in range(N):
    residue_OLD[i] = b[i]
    for j in range(N):
        residue_OLD[i] -= (matrix[i][j]*x_OLD[j])

    searchDirection_OLD[i] = residue_OLD[i]

while (errorNorm > 1e-10):
    alpha_num = 0.
    alpha_denom = 0.
    beta_num = 0.
    beta_denom = 0.
    errorNorm = 0.

    count += 1

    for i in range(N):
        alpha_num += residue_OLD[i]*residue_OLD[i]
        for j in range(N):
            alpha_denom += searchDirection_OLD[i]*matrix[i][j]*searchDirection_OLD[j]
    alpha = alpha_num/alpha_denom


    for i in range(N):
        x_OLD[i] += alpha*searchDirection_OLD[i]
        residue_NEW[i] = residue_OLD[i]
        for j in range(N):
            residue_NEW[i] -= (alpha*matrix[i][j]*searchDirection_OLD[j])

    for i in range(N):
        beta_num += residue_NEW[i]*residue_NEW[i]
        beta_denom += residue_OLD[i]*residue_OLD[i]

    beta = beta_num/beta_denom

    for i in range(N):
        searchDirection_NEW[i] = residue_NEW[i] + beta*searchDirection_OLD[i]
    #print(searchDirection_NEW)


    for i in range(N):
        residue_OLD[i] = residue_NEW[i]
        searchDirection_OLD[i] = searchDirection_NEW[i]

    # error = b - np.matmul(matrix, x_OLD)
    # errorNorm = np.linalg.norm(error)
    for i in range(N):
        error[i] = b[i]
        for j in range(N):
            error[i] -= matrix[i][j]*x_OLD[j]
        errorNorm += error[i]*error[i]

    errorNorm = errorNorm**0.5
    print(errorNorm)


    #print(x_OLD)
    if count > 4:
        print("Max iteration reached")
        break

print(count)
print('x with CG = \n')
print(x_OLD)
xReal = np.linalg.solve(matrix,b)
print('x with numpy = \n')
print(xReal)
