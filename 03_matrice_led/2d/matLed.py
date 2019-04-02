import i2cComm
import dicoMatrice2D
import time

#block = [0,1,1,0,0, 1,0,0,1,0, 1,1,1,1,0, 1,0,0,1,0, 1,0,0,1,0]

for matrice in dicoMatrice2D.dico2D.values():
    for ligne in matrice:
        for led in ligne
            i2cComm.writeNumber(data)
    time.sleep(1)