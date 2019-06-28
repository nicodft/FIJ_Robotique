maListe= []
texte = "une petite phrase"

print(maListe)

maListe.append (8)
maListe.append(5.6)
maListe.append(2)

print(maListe)

maListe.sort()

print (maListe)

texte = texte.replace("a", "i")
print(texte)

for element in texte:
    texte = texte.replace(element, "*")

print(texte)

phrase = "une/autre/phrase"
caractere = "éléphant"

phrase = phrase.replace("/", " ")

for accent in "éàè" : 
    caractere= caractere.replace(accent, "*")

print(phrase)
print(caractere)