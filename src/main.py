# ----------------------------------------------------------------------------
# A simple test for the button-bar (CircuitPython version)
#
# Author: Bernhard Bablok
# License: GPL3
#
# Website: https://github.com/bablokb/pcb-buttonbar
#
# ----------------------------------------------------------------------------

import board
import time
from digitalio import DigitalInOut, Direction

PIN_BTN2 = board.GP10
PIN_BTN5 = board.GP11
PIN_LED2 = board.GP12
PIN_LED5 = board.GP13

btn2 = DigitalInOut(PIN_BTN2)
btn2.direction = Direction.INPUT
btn2.pull = None

btn5 = DigitalInOut(PIN_BTN5)
btn5.direction = Direction.INPUT
btn5.pull = None

led2 = DigitalInOut(PIN_LED2)
led2.direction = Direction.OUTPUT

led5 = DigitalInOut(PIN_LED5)
led5.direction = Direction.OUTPUT

while True:
  if btn2.value:
    led2.value = 1 - led2.value    # toggle button
    time.sleep(0.15)               # a button-press takes about 100ms
  if btn5.value:
    led5.value = 1 - led5.value
    time.sleep(0.15)
