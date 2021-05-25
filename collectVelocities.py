from numpy import sqrt, array, correlate, arange, mean, loadtxt, savetxt, c_, split, swapaxes, trapz, transpose

start = 1
end = 5
size = 20000
vx = []
vy = []
vz = []

outputfile = 'collected_vneg' + str((end-start+1)*size) + '.txt'

for i in range(start, end + 1):
    inputfile = str(i) + '_20000/PSconfig/v_neg.txt'
    file = open(inputfile, 'r')
    Lines = file.readlines()



    for line in Lines:
        if not(line[0]=='#'):

            splitted = line.split()
            splitted = [float(i) for i in splitted] #split each line
            vx.append(splitted[0])
            vy.append(splitted[1])
            vz.append(splitted[2])

    file.close()



    # inputfile = str(i) + '_20000/PSconfig/v_pos.txt'
    # file = open(inputfile, 'r')
    # Lines = file.readlines()
    #
    #
    #
    # for line in Lines:
    #     if not(line[0]=='#'):
    #
    #         splitted = line.split()
    #         splitted = [float(i) for i in splitted] #split each line
    #
    # file.close()

vx = array(vx)
vy = array(vy)
vz = array(vz)

savetxt(outputfile, c_[vx,vy,vz])

vx = []
vy = []
vz = []

outputfile = 'collected_vpos' + str((end-start+1)*size) + '.txt'

for i in range(start, end + 1):
    inputfile = str(i) + '_20000/PSconfig/v_pos.txt'
    file = open(inputfile, 'r')
    Lines = file.readlines()



    for line in Lines:
        if not(line[0]=='#'):

            splitted = line.split()
            splitted = [float(i) for i in splitted] #split each line
            vx.append(splitted[0])
            vy.append(splitted[1])
            vz.append(splitted[2])

    file.close()



    # inputfile = str(i) + '_20000/PSconfig/v_pos.txt'
    # file = open(inputfile, 'r')
    # Lines = file.readlines()
    #
    #
    #
    # for line in Lines:
    #     if not(line[0]=='#'):
    #
    #         splitted = line.split()
    #         splitted = [float(i) for i in splitted] #split each line
    #
    # file.close()

vx = array(vx)
vy = array(vy)
vz = array(vz)

savetxt(outputfile, c_[vx,vy,vz])
