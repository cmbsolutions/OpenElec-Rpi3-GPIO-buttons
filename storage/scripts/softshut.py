#!/usr/bin/python
import sys
sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Set pin numbering to board numbering

in_pin = 23 # this is pin 16

GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:  
	print "Waiting for trigger, press CTRL+C to cancel."
	GPIO.wait_for_edge(in_pin, GPIO.RISING)
	os.system("shutdown -h now")
except KeyboardInterrupt:  
	GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
