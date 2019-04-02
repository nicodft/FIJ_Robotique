import i2cComm
import dicoMatrice2D
import time

<<<<<<< HEAD

for key,matrice in dicoMatrice2D.dico2D.items():
    print(key)
    for ligne in matrice:
        for led in ligne:
            i2cComm.writeNumber(led)
    time.sleep(3)
=======
#block = [0,1,1,0,0, 1,0,0,1,0, 1,1,1,1,0, 1,0,0,1,0, 1,0,0,1,0]

<<<<<<< HEAD
for element in dicoMatrice2D.dico2D:
    for data in element:
        i2cComm.writeNumber(data)
    time.sleep(1)
>>>>>>> Ajout du test de la matrice 2D
=======
for matrice in dicoMatrice2D.dico2D.values():
    for ligne in matrice:
        for led in ligne
            i2cComm.writeNumber(data)
    time.sleep(1)
>>>>>>> modif pour utiliser les dicos et tableaux
