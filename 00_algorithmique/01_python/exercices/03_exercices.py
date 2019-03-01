# Règles du jeu de la roulette ZCasino de OpenClassRooms.com
# On va simplifier les règles et je vous présente tout de suite ce que l'on obtient :

# Le joueur mise sur un numéro compris entre 0 et 49 (50 numéros en tout).
# En choisissant son numéro, il y dépose la somme qu'il souhaite miser.

# La roulette est constituée de 50 cases allant naturellement de 0 à 49.
# Les numéros pairs sont de couleur noire, les numéros impairs sont de couleur rouge.
# Le croupier lance la roulette, lâche la bille et quand la roulette s'arrête,
# relève le numéro de la case dans laquelle la bille s'est arrêtée.
# Dans notre programme, nous ne reprendrons pas tous ces détails « matériels » mais
# ces explications sont aussi à l'intention de ceux qui ont eu la chance d'éviter les salles de casino jusqu'ici.
# Le numéro sur lequel s'est arrêtée la bille est, naturellement, le numéro gagnant.

# Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible),
# le croupier lui remet 3 fois la somme misée.

# Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que
# le numéro gagnant (s'ils sont tous les deux pairs ou tous les deux impairs).
# Si c'est le cas, le croupier lui remet 50 % de la somme misée. Si ce n'est pas le cas, le joueur perd sa mise.

# Dans les deux scénarios gagnants vus ci-dessus
# (le numéro misé et le numéro gagnant sont identiques ou ont la même couleur),
# le croupier remet au joueur la somme initialement misée avant d'y ajouter ses gains.
# Cela veut dire que, dans ces deux scénarios, le joueur récupère de l'argent.
# Il n'y a que dans le troisième cas qu'il perd la somme misée.
# On utilisera pour devise le dollar $ à la place de l'euro pour des raisons d'encodage sous la console Windows.

# Attention, arrondir un nombre
# Vous l'avez peut-être bien noté, dans l'explication des règles je spécifiais que
# si le joueur misait sur la bonne couleur, il obtenait 50% de sa mise.
# Oui mais… c'est quand même mieux de travailler avec des entiers.
# Si le joueur mise 3$, par exemple, on lui rend 1,5$. C'est encore acceptable mais, si cela se poursuit,
# on risque d'arriver à des nombres flottants avec beaucoup de chiffres après la virgule.
# Alors autant arrondir au nombre supérieur. Ainsi, si le joueur mise 3$, on lui rend 2$.
# Pour cela, on va utiliser une fonction du module math nommée ceil.
# Je vous laisse regarder ce qu'elle fait, il n'y a rien de compliqué.













# SOLUTION ------------------------------------------------------------

import os

from random import randrange

from math import ceil


# Déclaration des variables de départ

argent = 1000 # On a 1000 $ au début du jeu

continuer_partie = True # Booléen qui est vrai tant qu'on doit

                        # continuer la partie


print("Vous vous installez à la table de roulette avec", argent, "$.")


while continuer_partie: # Tant qu'on doit continuer la partie

    # on demande à l'utilisateur de saisir le nombre sur

    # lequel il va miser

    nombre_mise = -1

    while nombre_mise < 0 or nombre_mise > 49:

        nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")

        # On convertit le nombre misé

        try:

            nombre_mise = int(nombre_mise)

        except ValueError:

            print("Vous n'avez pas saisi de nombre")

            nombre_mise = -1

            continue

        if nombre_mise < 0:

            print("Ce nombre est négatif")

        if nombre_mise > 49:

            print("Ce nombre est supérieur à 49")


    # À présent, on sélectionne la somme à miser sur le nombre

    mise = 0

    while mise <= 0 or mise > argent:

        mise = input("Tapez le montant de votre mise : ")

        # On convertit la mise

        try:

            mise = int(mise)

        except ValueError:

            print("Vous n'avez pas saisi de nombre")

            mise = -1

            continue

        if mise <= 0:

            print("La mise saisie est négative ou nulle.")

        if mise > argent:

            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")


    # Le nombre misé et la mise ont été sélectionnés par

    # l'utilisateur, on fait tourner la roulette

    numero_gagnant = randrange(50)

    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)


    # On établit le gain du joueur

    if numero_gagnant == nombre_mise:

        print("Félicitations ! Vous obtenez", mise * 3, "$ !")

        argent += mise * 3

    elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur

        mise = ceil(mise * 0.5)

        print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")

        argent += mise

    else:

        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")

        argent -= mise


    # On interrompt la partie si le joueur est ruiné

    if argent <= 0:

        print("Vous êtes ruiné ! C'est la fin de la partie.")

        continuer_partie = False

    else:

        # On affiche l'argent du joueur

        print("Vous avez à présent", argent, "$")

        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")

        if quitter == "o" or quitter == "O":

            print("Vous quittez le casino avec vos gains.")

            continuer_partie = False


# On met en pause le système (Windows)

os.system("pause")