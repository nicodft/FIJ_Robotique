from serial import Serial

comm = Serial()    # creation de l'objet associe au port serie
comm.baudrate = 115200     # definition du baudrate
comm.port = 'COM4'         # selection du port serie
comm.timeout = 1


imgA = [[0,0,1,0,0],
         [0,1,0,1,0],
         [1,0,0,0,1],
         [1,0,0,0,1],
         [1,0,0,0,1]]
comm.open()
for i in range(5):
    for j in range(5):
        comm.write(imgA[i][j])
        print(imgA[i][j])
comm.close()