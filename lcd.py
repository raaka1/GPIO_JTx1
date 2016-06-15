#!/usr/bin/env python
# Grovepi + grove RGB LCD module

import netifaces as ni
from lcd_driver import *

ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[2][0]['addr']

while(True):
    setText("SmartCow\n Tera+ Platform")
    setRGB(255, 102, 0)
    for c in range(0, 255):
        time.sleep(0.01)
    setText(ip)
    time.sleep(1.5)
