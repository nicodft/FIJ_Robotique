#import i2cComm
import time
import dicoMatrice2D

def envoiCaractere():

    matrice = dicoMatrice2D.dico2D[lettre]
    for ligne in matrice:
        for led in ligne :
               pass
            #i2cComm.writeNumber(led)

print("On va afficher la lettre a")
lettre=input()
dicoMatrice2D.testMatrice2D(lettre)

#envoiCaractere()

