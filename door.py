#!/usr/bin/python
import time
import RPi.GPIO as io
io.setmode(io.BCM)

pin_list = [ 21, 20, 26, 16 ]
for list in pin_list:
        io.setup(list, io.IN, pull_up_down=io.PUD_UP)

while True:
    for pin in pin_list:
        if io.input(pin):
		if pin == 26:
			print "Back door is open"
		if pin == 21:
			print "door1 is open"
		if pin == 20:
			print "door2 is open"
		if pin == 16:
			print "door3 is open"
#       else :
#               print("DOOR CLOSED", pin)


    time.sleep(1)
