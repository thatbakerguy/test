#!/usr/bin/python
# Example using a character LCD plate.
import time

import Adafruit_CharLCD as LCD
import os
from gps import *
from time import *
import time
import threading

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1.0, 1.0, 0.0)
lcd.clear()
gpsd = None #seting the global variabl

speed = gpsd.fix.speed

print speed
