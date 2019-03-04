class Voiture:

	def __init__(self):
		self.marque = "Ferrari"

class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.__prenom = prenom


class Robot:
    __erreur = "erreur, le robot n'est pas actif"

    def __init__(self, nom="robert", actif=False):
        self.__nom = nom
        self.__actif = actif
        self.__position = 0

    def parler(self):
        if self.__actif == True:
            print("Bonjour, je m'appelle",self.__nom)
        else:
            print(self.__erreur)

    def avancer(self, nombre):
        if self.__actif == True:
            print(self.__nom, "avance de ", nombre, "case")
            self.__position+=nombre
        else:
            print(self.__erreur)

robot1 = Robot()
robot2 = Robot("toto",False)
robot3 = Robot(actif=True)


robot1.parler()
robot1.avancer(5)

robot2.__erreur="yu"
robot2.parler()