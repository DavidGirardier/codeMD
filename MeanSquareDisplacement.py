import numpy as np

Nbig = 25
Nsmall = 100
inputfile = 'Trajectory.xyz'

xIniBig = np.zeros(Nbig)
yIniBig = np.zeros(Nbig)
zIniBig = np.zeros(Nbig)
xIniSmall = np.zeros(Nsmall)
yIniSmall = np.zeros(Nsmall)
zIniSmall = np.zeros(Nsmall)

xtBig = np.zeros(Nbig)
ytBig = np.zeros(Nbig)
ztBig = np.zeros(Nbig)
xtSmall = np.zeros(Nsmall)
ytSmall = np.zeros(Nsmall)
ztSmall = np.zeros(Nsmall)

Time = 10**25
file = open(inputfile, 'r')
Lines = file.readlines()
counter = -1
for t in range(0,Time,1):
    splitted = Lines[0].split()
    splitted = [float(i) for i in splitted]
    N = int(splitted[0])

    CountBig = -1
    CountSmall = -1

    

    # for k in range(3+t*(N+2),t*(N+2)+(N+2)):
    for k in range(N-1):
        splitted = Lines[k+t*(N+2)+2].split()
        xyzsplitted = [float(i) for i in splitted[1:]]
        name = splitted[0]
        x = xyzsplitted[0] 
        y = xyzsplitted[1] 
        z = xyzsplitted[2]
        
        if t == 0:
            if (name=='Big') :
                CountBig = CountBig + 1

                xIniBig[CountBig] = x
                yIniBig[CountBig] = y
                zIniBig[CountBig] = z
                #print(xyzsplitted[0])
            
            if (name=='Small') :
                
                CountSmall = CountSmall + 1

                xIniSmall[CountSmall] = x
                yIniSmall[CountSmall] = y
                zIniSmall[CountSmall] = z
    print(xIniBig)
        
    quit()       
