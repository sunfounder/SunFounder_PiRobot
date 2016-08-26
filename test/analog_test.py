#!/usr/bin/env python
'''
**********************************************************************
* Filename    : analog_test.py
* Description : analog port test  
* Author      : Dream
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-08-10 Change debug setting
*               Cavon    2016-08-23 Change I/O port
**********************************************************************
'''
from pirobot import PiRobot
import time

p = PiRobot()
p.DEBUG = True

def setup():
	print "===================================================="
	print "|                 Analog port 1 test               |"
	print "|--------------------------------------------------|"
	print "|      Potentionmeter  connect to analog 1         |"
	print "|                                                  |"
	print "|                        Read analog value                   |"
	print "|                                                  |"
	print "|                                        SunFounder|"
	print "===================================================="

def main():
	while True:
		A0 = p.read_analog(0)
		print A0
		time.sleep(0.5)

def destroy():
	pass

if __name__ == '__main__':
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()
	