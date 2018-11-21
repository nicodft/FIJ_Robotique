import SpyTank as spy
import RPi.GPIO as gpio
import time


SWITCH = 4
gpio.setmode(gpio.BCM)
gpio.setup(SWITCH, gpio.IN)

led = False

while True:
	if (gpio.input(SWITCH) == True):
		print("bouton enfonce")
		if led == True:
			led = False
		else:
			led = True
		spy.led(0, led)
		data = spy.litLigneGauche()
		print("Gauche : %i" % data)
		data = spy.litLigneDroite()
		print("Droite : %i" % data)
		time.sleep(1)
		