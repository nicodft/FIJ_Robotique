
#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print()
# and the integer division
# mind your parentheses!

########################################################################
# This library is used for communicating with the FIJ SpyTank
# History
# ------------------------------------------------
# Author	Date      		Comments
# M. Osee	07 Nov   18  	Creation, based on Gopigo lib
#
########################################################################

from I2C_comm import *

CMD_LED0 = 10
CMD_LED1 = 11
CMD_LED2 = 12
CMD_LED3 = 13

CMD_AVANCE = 1
CMD_RECULE = 2
CMD_DROITE = 3
CMD_GAUCHE = 4
CMD_STOP   = 5
CMD_MOTEURS = 6

CMD_LIGNE_G = 20
CMD_LIGNE_D = 21
CMD_ANALOG_READ = 22
CMD_LIT_DISTANCE = 23

def etatGauche():
	if litLigneGauche() > 300:
		return "noir"
	else:
		return "blanc"

def etatDroite():
	if litLigneDroite() > 300:
		return "noir"
	else:
		return "blanc"

# commande l'etat d'une LED
def led(ledNb, ledState):
    if ledNb == 0:
        sendCmd(CMD_LED0, ledState)
    elif ledNb == 1:
        sendCmd(CMD_LED1, ledState)
    elif ledNb == 2:
        sendCmd(CMD_LED2, ledState)
    elif ledNb == 3:
        sendCmd(CMD_LED3, ledState)


# fait avancer le SpyTank a une vitesse donnee
def avance(speed):
	return sendCmd(CMD_AVANCE, speed)

# fait reculer le SpyTank a une vitesse donnee
def recule(speed):
	return sendCmd(CMD_RECULE, speed)

# fait tourner le SpyTank a droite a une vitesse donnee
def droite(speed):
	return sendCmd(CMD_DROITE, speed)

# fait tourner le SpyTank a gauche a une vitesse donnee
def gauche(speed):
	return sendCmd(CMD_GAUCHE, speed)

# Stoppe le SpyTank
def stop():
	return sendCmd(CMD_STOP)

# fait tourner le SpyTank a gauche a une vitesse donnee
def vitMoteurs(vitesseGauche, vitesseDroite):
	return sendCmd(CMD_MOTEURS, vitesseGauche, vitesseDroite)
	
def litLigneDroite():
	sendCmd(CMD_LIGNE_D);
	time.sleep(0.1)
	try:
		b0 = bus.read_byte(address)
		# print("ID: %i" % b0)
		b1 = bus.read_byte(address)
		b2 = bus.read_byte(address)
	except IOError:
		return -1
	return b1*256 + b2

def litLigneGauche():
	sendCmd(CMD_LIGNE_G);
	time.sleep(0.1)
	try:
		b0 = bus.read_byte(address)
		# print("ID: %i" % b0)
		b1 = bus.read_byte(address)
		b2 = bus.read_byte(address)
	except IOError:
		return -1
	return b1*256 + b2
	
def analogRead(Ain):
	sendCmd(CMD_ANALOG_READ, Ain);
	time.sleep(0.1)
	try:
		b0 = bus.read_byte(address)
		# print("ID: %i" % b0)
		b1 = bus.read_byte(address)
		b2 = bus.read_byte(address)
	except IOError:
		return -1
	return b1*256 + b2
	
def litDistance():
	sendCmd(CMD_LIT_DISTANCE);
	time.sleep(0.2)
	try:
		b0 = bus.read_byte(address)
		# print("ID: %i" % b0)
		b1 = bus.read_byte(address)
		b2 = bus.read_byte(address)
	except IOError:
		return -1
	return b1*256 + b2

