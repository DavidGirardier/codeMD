import numpy as np
from scipy.interpolate import SmoothBivariateSpline, RectBivariateSpline
import matplotlib.pyplot as plt
import glob
import pickle
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

with open('spline.pkl', 'rb') as f:
    loaded_spline = pickle.load(f)

inputfile= 'traj/ntraj10000_Z1g1.0m1.0'

plotting_option=False
files= glob.glob(inputfile+'*')

every = 1
x=[]
x2=[]
y=[]
xpy=[]
xpy2=[]
xty=[]
comm=[]
count=0
for j in files:
    trajectory = np.loadtxt(j)
    count=count+1
    #print(j)
    for l in range(len(trajectory[:,0])):

        #print(spline(trajectory[l,1],trajectory[l,2])[0][0])
        comm_val = loaded_spline(trajectory[l,1],trajectory[l,2])[0][0]
        # if comm_val > 0.01 and comm_val < 0.99:
        if l%every == 0:
            comm.append(comm_val)
            x.append(trajectory[l,1])
            #xpy.append(0.5*trajectory[l,1]+ 0.5*trajectory[l,2])
            # x2.append(trajectory[l,1]**3)
            y.append(trajectory[l,2])
            # xpy.append(0.8*trajectory[l,1]+ 0.2*trajectory[l,2])
            # xpy2.append(0.9*trajectory[l,1]+ 0.1*trajectory[l,2])
            # xty.append(trajectory[l,1]*trajectory[l,2])
    if count== 100 : break


def sigmoid(x, x0, k):
        return 1 / (1 + np.exp(-abs(k) * (x - x0)))

ratio_list = np.linspace(0,1.0,101)
# ratio_list = [0, 0.13, 0.3]
mse_list = []
for ratio in ratio_list:
    x_data = -1.0*(ratio * np.array(x) + (1.0-ratio)*np.array(y))
    y_data = comm


    

    # Fit the sigmoid function to the data
    popt, _ = curve_fit(sigmoid, x_data, y_data, p0=[0.0,1.0])

    # Extract the fitted parameters
    x0, k = popt
    #print(f"Fitted parameters: x0={x0}, k={k}")

    # Compute the fitted values
    y_fitted = sigmoid(x_data, *popt)

    # Calculate the Mean Squared Error
    mse = mean_squared_error(y_data, y_fitted)
    mse_list.append(mse)
    # print(ratio)
    print(f,f"MSE: {mse}, for ratio {ratio}")

    # Plot the data points and the fitted curve (optional)
    import matplotlib.pyplot as plt

    if plotting_option == True:
        x_plot = np.linspace(-1.5,1.5,100)
        plt.scatter(x_data[::10], y_data[::10], label="Data", color="red")

        plt.plot(x_plot, sigmoid(x_plot,x0,k), label="Fitted Sigmoid", color="blue")
        #plt.legend()
        plt.xlabel("x")
        plt.ylabel("Committor")
        plt.title("Sigmoid Fit to Data")
        plt.savefig("plot/comm_ratio"+str(ratio)+".eps")
        plt.clf()
    # plt.show()

outputName = "msebyratio"
np.savetxt(outputName, np.c_[ratio_list,mse_list])




# outputName = 'commbyq'
# np.savetxt(outputName, np.c_[x,comm])

# plt.plot(x,comm, '.',label='x')
# #plt.plot(y,comm, '.', label='y')
# # plt.plot(x2,comm, '.', label='x3')
# #plt.plot(xpy2,comm, '.',label='0.9x+0.1y')
# #plt.plot(xpy,comm, '.',label='0.8x+0.2y')
# # plt.plot(xty,comm, '.')
# plt.xlabel('Commitor')
# plt.ylabel('cv')
# plt.legend()
# plt.show()



    

