#!/bin/python

# it's messy; it might not work; but aren't we here to learn?

import RPi.GPIO as GPIO

# use Broadcom (BCM) pin numbering
GPIO.setmode(GPIO.BCM)

# set the pin high by default
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    # use edge detection to see if pin is pulled low
    GPIO.wait_for_edge(17, GPIO.FALLING)
    print "Button pressed!"
    
except:
    pass


#clean up clean up everybody clean up
GPIO.cleanup()
