# type() permet de connaitre le type d'une variable
# print() permet d'afficher quelque chose dans un terminal

# EXEMPLE 1 ---------------------------------------------
# On affiche "hello world" dans le terminal. Ensuite,
# on demande d'afficher le type de "5" qui est ici encode comme du texte
print("hello world")
print( type("5") )


# EXEMPLE 2 ---------------------------------------------
# On cree no variables de differents type
nombreEntier = 5
nombreVirgule = 5.6
texte = "yolooo !"
boolean = True
liste = ["1er element", "2eme element"]

# On demande d'afficher le type de chaque variable dans le terminal
print(type(nombreEntier)) #entier : int pour integer
print(type(nombreVirgule)) #virgule : float
print(type(texte)) # texte : str pour string
print(type(boolean)) # boolean : bool
print(type(liste)) # liste : list

# Ici, on demande d'afficher les different elements de notre liste
print(liste[0]) # affiche "1er element"
print(liste[1]) # affiche "2eme element"


# EXEMPLE 3 ---------------------------------------------
# Les differents operateurs arithmetique
# * multiplication
# / division
# // division entière
# - soustraction
# + addition
# % modulo
# ** exposant


print (5*3)
result = nombreEntier * nombreVirgule
print(result)

print(10%3)

print(5**2)


# EXEMPLE 4 ---------------------------------------------
# Pour modifier le type d'une variable, on utilise le cast
variable = "5"
print(type(variable)) # On demade d'afficher le type de la vraiable. Ici, c'est un str

variable = int(variable) # on change son type en int

print(type(variable))

variable = float(variable) # on change son type en float

print(type(variable))

variable = str(variable) # on rechange son type en str

print(type(variable))



