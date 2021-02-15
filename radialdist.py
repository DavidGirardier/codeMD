import numpy as np

## Input
box = 39.43023755756404
nhist = 200
delg =0.0

##Read File

file = open('trajectories.out', 'r')
Lines = file.readlines()
part=[]
sample = []
nsample =0
npart= 250
counter=0
stop=10000
for line in Lines:

    if not(line[0]=='#'):
        counter = counter + 1
        splitted = line.split()
        splitted = [float(i) for i in splitted] #split each line
        part.append(splitted[:]) #Make a matrix made of each positions

        if (counter%npart==0):
            sample.append(part[:][:]) #Add each matrix pos to a list made of each time step
            nsample = nsample + 1
            part = []
    if nsample == stop:
        break
##Initialisation

delg = box/(2*nhist) #step between each r
gNaCl=np.zeros(nhist)
gNaNa=np.zeros(nhist)
gClCl=np.zeros(nhist)
radius = np.zeros(nhist)



## Sample

for h in range(nsample):
    for i in range(npart-1):                #loop over all particle pairs
        for j in range((i + 1),npart):

            if (i < (npart/2)) & (j >= (npart/2)):  #Na-Cl
                xr = sample[h][i][0] - sample[h][j][0] # Calculate the difference
                xr = xr - box*round(xr/box)             # Reduce it with respect to periodic boundary condition
                yr = sample[h][i][1] - sample[h][j][1]
                yr = yr - box*round(yr/box)
                zr = sample[h][i][2] - sample[h][j][2]
                zr = zr - box*round(zr/box)
                r = (xr**2 + yr**2 + zr**2)**0.5
                if r < box/2 :
                    ig = int(r/delg)
                    gNaCl[ig]= gNaCl[ig] + 2 #count the pair

            if (i < (npart/2)) & (j < (npart/2)): #Na-Na
                xr = sample[h][i][0] - sample[h][j][0]
                xr = xr - box*round(xr/box)
                yr = sample[h][i][1] - sample[h][j][1]
                yr = yr - box*round(yr/box)
                zr = sample[h][i][2] - sample[h][j][2]
                zr = zr - box*round(zr/box)
                r = (xr**2 + yr**2 + zr**2)**0.5
                if r < box/2 :
                    ig = int(r/delg)
                    gNaNa[ig]= gNaNa[ig] + 2

            if (i >= (npart/2)) & (j >= (npart/2)): #Cl-Cl
                xr = sample[h][i][0] - sample[h][j][0]
                xr = xr - box*round(xr/box)
                yr = sample[h][i][1] - sample[h][j][1]
                yr = yr - box*round(yr/box)
                zr = sample[h][i][2] - sample[h][j][2]
                zr = zr - box*round(zr/box)
                r = (xr**2 + yr**2 + zr**2)**0.5
                if r < box/2 :
                    ig = int(r/delg)
                    gClCl[ig]= gClCl[ig] + 2

## Histogram
histfile = open('histfile.dat','w')
histfile.write('#Radial distribution function \n #x \t y_Na-Cl \t y_Na-Na \t y_Cl-Cl \n')
density = (npart) / (box**3)
density2 = (npart/2) / (box**3) #half of normal density because pairs of same specie
for i in range(nhist):
    radius[i] = delg*(i+0.5)
    volume_bin = ((i+1)**3 - i**3)*delg**3
    nidealgas = (4.0/3.0)*np.pi*volume_bin*density  #Number of particle if it was a rare gas
    nidealgas2 = (4.0/3.0)*np.pi*volume_bin*density2
    gNaCl[i] = gNaCl[i] /(nsample*(npart/2)*nidealgas) #Normalize   #npart/2 because it has to be related to one particle
    gNaNa[i] = gNaNa[i] /(nsample*(npart/2)*nidealgas2)
    gClCl[i] = gClCl[i] /(nsample*(npart/2)*nidealgas2)
    histfile.write(str(radius[i])+ '\t' + str(gNaCl[i])+ '\t' + str(gNaNa[i]) + '\t' + str(gClCl[i]) + '\n')
histfile.close
