#!/usr/bin/python
 
import Adafruit_CharLCD as LCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
 
lcd = LCD.Adafruit_CharLCDPlate()
 
cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f2"
 
lcd.set_color(1.0, 1.0, 0.0)
 
def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output
 
while 1:
        lcd.clear()
        ipaddr = run_cmd(cmd)
        print ipaddr
        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        lcd.message('IP %s' % ( ipaddr ) )
        sleep(2)
