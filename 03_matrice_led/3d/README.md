<<<<<<< HEAD
# Matrice LED 3D
=======
Matrice LED 3d
>>>>>>> ajout documentation et readme matrice

un "cube" de 3*3*5 led
On parcourt par colonne (9 au total)

<<<<<<< HEAD
fournir dico [lettre, matrice binaire] (binaire 45 element, matrice par plan (5 plans)) pour l'arduino)

une fonction intensite qui prend en paramettre un charactere et une intensite comprise entre 1 et 5
un fonction pulse qui prend en parametre la vitesse de pulsation comprise entre 1 et 5 qui permet de faire pulser l'afficher

=======
une fonction qui prend un charactere en parametre et qui renvois sa valeur ASCII
une fonction intensite qui prend en paramettre un charactere et une intensite comprise entre 1 et 5
un fonction pulse qui prend en parametre la vitesse de pulsation comprise entre 1 et 5 qui permet de faire pulser l'afficher

librairie translate qui permet de "traduire" l'ASCII en liste de binaire (45, compte par colonne et par plan verticale) pour l'arduino

>>>>>>> ajout documentation et readme matrice
On utilise ensuite la fonction de trasmission a l'arduino