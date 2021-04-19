import numpy as np

oldfile = open('data.inpt', 'r')
newfile = open('checkpoint.txt', 'w')

#angtoau_factor = 1.8897261254535
#veltoau_factor = 1.8897261254535/(4.1341373336493*(10**3))
autolambda = 1.0/(1.8897261254535*0.317)
autolambdavel = autolambda * 41.341374575751 * 7.026280076
initialbox = 39.43023755756404
natom = 250
Lines = oldfile.readlines()
arr = []
count = -1

for line in Lines:
    count = count + 1
    #print(line)
    #print line.split(" ")
    splitted = line.split()
    splitted = [float(i) for i in splitted] #0-124 pos Na, 125-249 pos Cl , 250-374 v Na, 375-499 v Cl
    arr.append(splitted[:])

#print(arr[:])
newfile.write(str(natom) +'\t'+ str(initialbox*autolambda) +'\n')
for i in range(125):
    newfile.write(str(arr[i+125][0]*autolambda) +'\t'+ str(str(arr[i+125][1]*autolambda)) +'\t'+ str(arr[i+125][2]*autolambda) + '\t'+ str(arr[i+375][0]*autolambdavel) +'\t'+ str(str(arr[i+375][1]*autolambdavel)) +'\t'+ str(arr[i+375][2]*autolambdavel) +'\t'+ str(arr[i+125][0]*autolambda) +'\t'+ str(str(arr[i+125][1]*autolambda)) +'\t'+ str(arr[i+125][2]*autolambda) + '\t'+ str(arr[i+375][0]*autolambdavel) +'\t'+ str(str(arr[i+375][1]*autolambdavel)) +'\t'+ str(arr[i+375][2]*autolambdavel) + '\n')
    newfile.write(str(arr[i][0]*autolambda) +'\t'+ str(str(arr[i][1]*autolambda)) +'\t'+ str(arr[i][2]*autolambda) +'\t' + str(arr[i+250][0]*autolambdavel) +'\t'+ str(str(arr[i+250][1]*autolambdavel)) +'\t'+ str(arr[i+250][2]*autolambdavel) +'\t'+ str(arr[i][0]*autolambda) +'\t'+ str(str(arr[i][1]*autolambda)) +'\t'+ str(arr[i][2]*autolambda) + '\t'+ str(arr[i+250][0]*autolambdavel) +'\t'+ str(str(arr[i+250][1]*autolambdavel)) +'\t'+ str(arr[i+250][2]*autolambdavel) + '\n')

newfile.close()
