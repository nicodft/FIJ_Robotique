import i2cComm
import dicoMatrice2D
import time

#block = [0,1,1,0,0, 1,0,0,1,0, 1,1,1,1,0, 1,0,0,1,0, 1,0,0,1,0]

for element in dicoMatrice2D.dico2D:
    for data in element:
        i2cComm.writeNumber(data)
    time.sleep(1)