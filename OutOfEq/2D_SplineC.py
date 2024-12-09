import numpy as np
from scipy.interpolate import SmoothBivariateSpline, RectBivariateSpline,interp2d
import matplotlib.pyplot as plt
import glob
import pickle

def cubic_spline_interpolation(x_values, y_values, z_values):
    # Flatten the input arrays
    x_flat = x_values.flatten()
    y_flat = y_values.flatten()
    z_flat = z_values.flatten()

    # Perform cubic spline interpolation
    spline = SmoothBivariateSpline(y_flat, x_flat, z_flat, s=0.1, kx=3, ky=3)

    # Create a grid for the interpolation
    x_grid = np.linspace(x_values.min(), x_values.max(), 100)
    y_grid = np.linspace(y_values.min(), y_values.max(), 100)
    x_grid, y_grid = np.meshgrid(x_grid, y_grid)

    # Evaluate the spline on the grid
    z_interp = spline.ev(y_grid.ravel(), x_grid.ravel()).reshape(x_grid.shape)

    # Create surface plot using Plotly
    surface_plot = go.Figure(data=[go.Surface(z=z_interp.T, y=y_grid,  x=x_grid)])
    surface_plot.update_layout(title='Cubic Spline Interpolated Surface', autosize=False,
                               width=700, height=700,
                               margin=dict(l=65, r=50, b=65, t=90))

    # Create contour plot using Plotly
    contour_plot = go.Figure(data=go.Contour(z=z_interp.T,  y=y_grid[:,0],x=x_grid[0], ncontours=30))
    contour_plot.update_layout(title='Contour Plot', autosize=False,
                               width=700, height=700,
                               margin=dict(l=65, r=50, b=65, t=90))

    return surface_plot, contour_plot, spline


filename = '../comm_Z1g50.0ntraj1000'
z = np.loadtxt(filename)  # Example data for z

with open(filename, "r") as file:
    first_line = file.readline().strip()
    values = first_line[1:].strip().split()
    head = [float(value) for value in values]



xrange = (head[0],head[1])
yrange = (head[2],head[3])

npointsx = int(head[4])
npointsy = int(head[5])


x_values = np.linspace(xrange[0], xrange[1], npointsx)
y_values = np.linspace(yrange[0], yrange[1], npointsy)

x, y = np.meshgrid(x_values, y_values)

x_flat = x.flatten()
y_flat = y.flatten()
z_flat = z.flatten()

# Perform cubic spline interpolation

#spline = SmoothBivariateSpline(y_flat, x_flat, z_flat, kx=3, ky=3)
#spline = RectBivariateSpline(x_values, y_values, z, kx=3, ky=3, s=0.)
spline = RectBivariateSpline(x_values, y_values, z, kx=1, ky=1, s=0.)
#spline = interp2d(x_values, y_values, z, kind='linear', copy=True, bounds_error=False, fill_value=None)
val_spline = []
for i in x_values:
    for j in y_values: 
    
        val_spline.append(spline(i,j))
val_spline = np.array(val_spline)
matrixS=val_spline.reshape(npointsx, npointsy)
S_flat = matrixS.flatten()
# for i in range(len(S_flat)):
#     if S_flat[i] < 0 : print("aie")
# print(val_spline<0)
# exit()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot the first 2D colormap on the first subplot (ax1)
im1 = ax1.imshow(np.transpose(z), extent=[x_values.min(), x_values.max(), y_values.min(), y_values.max()],
                 origin='lower', cmap='viridis', aspect='auto')
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("Numerical Committor")
#fig.colorbar(im1, ax=ax1)  # Color bar for the first subplot

# Plot the second 2D colormap on the second subplot (ax2)
im2 = ax2.imshow(np.transpose(matrixS), extent=[x_values.min(), x_values.max(), y_values.min(), y_values.max()],
                 origin='lower', cmap='viridis', aspect='auto')
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("Interpolated Committor")
fig.colorbar(im2, ax=ax2, label='Committor Values')  # Color bar for the second subplot

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
with open(filename+'_spline.pkl', 'wb') as f:
    pickle.dump(spline, f)


 


# with open('spline.pkl', 'rb') as f:
#     loaded_spline = pickle.load(f)
# folder="traj/"
inputfile= 'ntraj10000_Z1g5.0m1.0'

files= glob.glob(inputfile+'*')



for j in files:
    # traj_path=folder+j
    trajectory = np.loadtxt(j)
    comm_traj=[]
    comm_time=[]
    print(j)
    for l in range(len(trajectory[:,0])):

        #print(spline(trajectory[l,1],trajectory[l,2])[0][0])
        comm_traj.append(spline(trajectory[l,1],trajectory[l,2])[0][0])
        comm_time.append(trajectory[l,0])
    
    outputName = 'comm_' + j 
    np.savetxt(outputName, np.c_[comm_time,comm_traj])

    

