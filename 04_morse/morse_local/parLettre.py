#coding: utf-8

import dicoMatrice2D
import comMorse

print ("tape un code morse")
code = input()
reponse = comMorse.decode(code)
dicoMatrice2D.testMatrice2D(reponse)