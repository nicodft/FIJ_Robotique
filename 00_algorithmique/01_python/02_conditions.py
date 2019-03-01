# input("message")
# if : si
# elif : sinon si
# else : sinon

# les different operateurs de comparaison
# == egale
# != different
# <> different
# > plus grand
# >= plus grand ou egale
# < plus petit
# <= plus petit ou egale


nombre = -5
# On verifie ici si le nombre est + grand que 0 ou
# sinon si il est + petit que 0 ou
# sinon, c'est qu'il est egal a 0
if nombre > 0 :
    print("ton nombre est plus grand que 0")
elif nombre < 0 :
    print("ton nombre est plus  petit que 0")
else :
    print("ton nombre est egal a 0")


# Avec le modulo, on verifie si le nombre est pair ou sinon impair
if nombre%2 == 0 :
    print("le nombre est pair")
else :
    print("le nombre est impair")