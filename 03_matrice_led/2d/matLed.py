import i2cComm
import dicoMatrice2D
import time


for key,matrice in dicoMatrice2D.dico2D.items():
    print(key)
    for ligne in matrice:
        for led in ligne:
            i2cComm.writeNumber(led)
    time.sleep(3)
