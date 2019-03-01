<<<<<<< HEAD
# Matrice LED 2d

5 colonnes
5 lignes

fournir dico [lettre, matrice binaire] (binaire 15 element compte par ligne) pour l'arduino)

une fonction intensite qui prend en paramettre un charactere et une intensite comprise entre 1 et 5
une fonction pulse qui prend en parametre la vitesse de pulsation comprise entre 1 et 5 qui permet de faire pulser les LED

On utilise ensuite la fonction de traesmission a l'arduino

matLedAlpha.ino permet de tester la matrice 2D connectée à l'Arduino seul.
matLed2dComm.ino affiche "l'image" transmise par la Raspberry Pi.
=======
Matrice LED 2d

3 colonnes
5 lignes

une fonction qui prend un charactere en parametre et qui renvois sa valeur ASCII
une fonction intensite qui prend en paramettre un charactere et une intensite comprise entre 1 et 5
un fonction pulse qui prend en parametre la vitesse de pulsation comprise entre 1 et 5 qui permet de faire pulser l'afficher

librairie translate qui permet de "traduire" l'ASCII en liste de binaire (15, compte par colonne) pour l'arduino

On utilise ensuite la fonction de trasmission a l'arduino
>>>>>>> ajout documentation et readme matrice
