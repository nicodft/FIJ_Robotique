import i2cComm
import dicoMatrice3D
import time


for key,matrice in dicoMatrice3D.dico3D.items():
    print(key)
    for plan in matrice:
        for ligne in plan:
            for led in ligne:
                i2cComm.writeNumber(led)
    time.sleep(3)
