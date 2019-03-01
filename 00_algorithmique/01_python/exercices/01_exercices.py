# les import permettent d'avoir des fonctions toute faite.
# Il faut voir ca comme une feuille contenant plein de fonctions qu'on peut appeler quand on a fait le lien
# os nous permet d'avoir acces a pause pour les systemes windows qui n'attendent pas qu'on lise la fin du programme
# random permet d'avoir acces a des fonction pour cree des nombres aleatoires
import os
import random

# Creation d'un nombre aleatoire compris entre 0 et 10
nombre = random.randrange(10)
print("Jeu du + OU - ? Devine le nombre auquel je pense, entre 1 et 10")
reponse = -1 # pour eviter que le programe trouve directement la reponse

# Tant que la reponse est differente de nombre, la boucle continue
while reponse != nombre :
  print("Tape un nombre entier entre 0 et 10")
  reponse =int(input()) # ici on change directement le type de l'entree clavier en int

  if reponse > nombre :
    print ("moins :-( ")
  elif reponse < nombre :
    print ("plus :-(D ")
  else :
    print ("Yes :-) , le nombre =  ", nombre)
  
# os.system("pause") # Pour Windows, il faut retirer le # en debut de ligne