#!/usr/bin/env python
'''
**********************************************************************
* Filename    : led_test.py
* Description : led test
* Author      : Dream
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-07-28 New version
*               Cavon    2016-08-23 Update set debug
**********************************************************************
'''
from pismart.led import LED
import time

blue_leds = LED(LED.BLUE)
blue_leds.DEBUG = 4

red_leds  = LED(LED.RED)
red_leds.DEBUG = 4

LED_MAX = 100
LED_MIN = 10

def setup():
	print "|=====================================================|"
	print "|                   LED Ring test                     |"
	print "|-----------------------------------------------------|"
	print "|                                                     |"
	print "|         Breath Blue leds breath and then Red leds   |"
	print "|                                                     |"
	print "|                                           SunFounder|"
	print "|=====================================================|"
	time.sleep(2)

def main():
	while True:
		for x in xrange(1,3):
			for x in xrange(LED_MIN, LED_MAX, 2):
				blue_leds.brightness = x
				time.sleep(0.03)
			for x in xrange(LED_MAX, LED_MIN, -1):
				blue_leds.brightness = x
				time.sleep(0.05)
		blue_leds.off()

		for x in xrange(1,3):
			for x in xrange(LED_MIN, LED_MAX, 2):
				red_leds.brightness = x
				time.sleep(0.03)
			for x in xrange(LED_MAX, LED_MIN, -1):
				red_leds.brightness = x
				time.sleep(0.05)
		red_leds.off()

def destroy():
	red_leds.off()
	blue_leds.off()

if __name__ == '__main__':
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()
