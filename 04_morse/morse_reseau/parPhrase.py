# coding: utf-8

import comMorse

def texte(phrase):
    reponse=""
    for lettre in phrase:
        if lettre != " " and lettre != "":
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
            elif element == "/":
                reponse= reponse + " "
            else:
                pass
    return reponse