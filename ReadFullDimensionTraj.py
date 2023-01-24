import numpy as np


timestep= 1.




centerOfMassA=[0.0,0.0,0.0]
centerOfMassB=[0.0,0.0,0.0]
counter = 0
distanceCenterOfMass=[]
inputfile = 'trajFull5ns.txt'
with open(inputfile) as FileObj:
    for lines in FileObj:

        counter = counter + 1
        splitted = lines.split()
        position = [float(i) for i in splitted[3:6]]
        
        
        if splitted[0] == '1C60A':
            centerOfMassA[0] = centerOfMassA[0] + position[0]
            centerOfMassA[1] = centerOfMassA[1] + position[1]
            centerOfMassA[2] = centerOfMassA[2] + position[2]
            

        elif splitted[0] == '2C60B':
            centerOfMassB[0] = centerOfMassB[0] + position[0]
            centerOfMassB[1] = centerOfMassB[1] + position[1]
            centerOfMassB[2] = centerOfMassB[2] + position[2]

        else:
            
            print('ligne ' + str(counter)+ ' : ' + str(lines))
            print(counter)
            centerOfMassA = [m/60.0 for m in centerOfMassA]
            centerOfMassB = [m/60.0 for m in centerOfMassB]
            # print(centerOfMassA)
            # print(centerOfMassB)
            rAB = [centerOfMassA[0]-centerOfMassB[0], centerOfMassA[1]-centerOfMassB[1], centerOfMassA[2]-centerOfMassB[2]]
            #print(rAB)
            distanceCenterOfMass.append(np.linalg.norm(rAB))
            centerOfMassA=[0.0,0.0,0.0]
            centerOfMassB=[0.0,0.0,0.0]
            

            
outputName = 'CV.txt'
time = [i*timestep for i in range(len(distanceCenterOfMass))]
np.savetxt(outputName, np.c_[time, distanceCenterOfMass], fmt='%1.8E')


exit()





np.savetxt(outputName, np.c_[[t*newdt for t in range(int(tFile/newdt) + 1)], XAC], fmt='%1.8E')

#print(np.mean([[2,2], [1,1]], axis=0))




