# coding: utf-8

import comMorse

print("entrez un caractere")
lettre = input()
resultat = comMorse.encode(lettre)
print (resultat)


print("entrez un code morse")
codeMorse = input()
resultat = comMorse.decode(codeMorse)
print (resultat)