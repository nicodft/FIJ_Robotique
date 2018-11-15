
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

CMD_LED1 = 10
CMD_LED2 = 11
CMD_LED3 = 12
CMD_LED4 = 13

CMD_AVANCE = 1
CMD_RECULE = 2
CMD_DROITE = 3
CMD_GAUCHE = 4
CMD_STOP   = 5

CMD_LIGNE_D = 20
CMD_LIGNE_G = 21


# commande l'etat d'une LED
def led(ledNb, ledState):
    if ledNb == 1:
        sendCmd(CMD_LED1, ledState)
    elif ledNb == 2:
        sendCmd(CMD_LED2, ledState)
    elif ledNb == 3:
        sendCmd(CMD_LED3, ledState)
    elif ledNb == 4:
        sendCmd(CMD_LED4, ledState)


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

def litLigneDroite():
	sendCmd(CMD_LIGNE_D);
	time.sleep(0.1)
	try:
		b1 = bus.read_byte(address)
		b2=bus.read_byte(address)
	except IOError:
		return -1
	return b1*256 + b2




# # Arduino Digital Read
# def digitalRead(pin):
# 	if pin ==10 or pin ==15 or pin ==0 or pin ==1:
# 		write_i2c_block(address, digital_read_cmd + [pin, unused, unused])
# 		time.sleep(.1)
# 		n=bus.read_byte(address)
# 		bus.read_byte(address)		#Empty the buffer
# 		return n
# 	else:
# 		return -2

# # Arduino Digital Write
# def digitalWrite(pin, value):
# 	#if pin ==10 or pin ==0 or pin ==1 or pin==5 or pin ==16 or pin==17 :
# 	if value==0 or value ==1:
# 		write_i2c_block(address, digital_write_cmd + [pin, value, unused])
# 		# time.sleep(.005)	#Wait for 5 ms for the commands to complete
# 		return 1
# 	#else:
# 	#	return -2
