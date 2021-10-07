#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# A simple test for the button-bar
#
# Author: Bernhard Bablok
# License: GPL3
#
# Website: https://github.com/bablokb/pcb-buttonbar
#
# ----------------------------------------------------------------------------

from gpiozero import Button, LED
import signal

btn2 = Button(24,pull_up=None,active_state=True)
btn5 = Button(23,pull_up=None,active_state=True)

led2 = LED(17)
led5 = LED(27)

btn2.when_pressed = lambda: led2.toggle()
btn5.when_pressed = lambda: led5.toggle()

signal.pause()
