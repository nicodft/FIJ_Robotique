# coding: utf-8

import comMorse

def texte(phrase):
    reponse=""
    for lettre in phrase:
        if lettre != " ":
            reponse= reponse + comMorse.encode(lettre)
            reponse= reponse + " "
        else:
            reponse= reponse + "/ "
    return reponse



def morse(morseBrut):
    reponse=""
    morseBrut = str.split(morseBrut," ")
    for element in morseBrut:
            if element != "/" and element != "":
                reponse= reponse + comMorse.decode(element)
            else:
                reponse= reponse + " "
    return reponse

print("tapez un mot ou une phrase courte")
phrase = input()
print(texte(phrase))

print("tapez un mot ou une phrase courte en morse")
morseBrut = input()
print(morse(morseBrut))