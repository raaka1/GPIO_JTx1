#!/usr/bin/env python
#
# GrovePi Example for using the Grove - LCD RGB Backlight (http://www.seeedstudio.com/wiki/Grove_-_LCD_RGB_Backlight)
# -- Ravi Kiran. K added support for Jetson TK1 and TX1
# sudo pip install netifaces

import sys
import time

import smbus

bus = smbus.SMBus(1)  # pin 27-28

# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

# set backlight to (R,G,B) (values from 0..255 for each)


def setRGB(r, g, b):
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0, 0)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 1, 0)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x08, 0xaa)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 4, r)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 3, g)
    bus.write_byte_data(DISPLAY_RGB_ADDR, 2, b)

# send command to display (no need for external use)


def textCommand(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, cmd)

# set display text \n for second line(or auto wrap)


def setText(text):
    textCommand(0x01)  # clear display
    time.sleep(.05)
    textCommand(0x08 | 0x04)  # display on, no cursor
    textCommand(0x28)  # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(c))

# Update the display without erasing the display


def setText_norefresh(text):
    textCommand(0x02)  # return home
    time.sleep(.05)

    textCommand(0x08 | 0x04)  # display on, no cursor
    textCommand(0x28)  # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(c))
