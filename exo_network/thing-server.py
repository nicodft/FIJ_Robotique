
#on importe les librairies dont on aura besoin
import RPi.GPIO as GPIO
import time
import network

SWITCH = #a definir
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN)


