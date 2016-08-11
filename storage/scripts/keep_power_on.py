#!/usr/bin/python
import sys
sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # Set pin numbering to board numbering

out_pin = 24 # this is pin 18

GPIO.setup(out_pin, GPIO.OUT, initial=GPIO.HIGH)
