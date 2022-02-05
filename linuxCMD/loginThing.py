

import time
from adafruit_hid.keycode import Keycode
from _init import kbd,mouse,bt1,bt2,bt3,bt4,led
from common.tool import FIX_Waiting, stringTokey

loopSec = 1
finishSec = 0.2

def commonLogin():
    stringTokey(kbd,"ubuntu\r",FIX_Waiting,0.03)
    time.sleep(1)
    stringTokey(kbd,"d52180362\r",FIX_Waiting,0.02)
    time.sleep(1)
    stringTokey(kbd,"ifconfig\r",FIX_Waiting,0.01)
    time.sleep(1)


def loop():
    while True:
        time.sleep(loopSec)
        if not bt1.value:
            led.value = 0
            kbd.send(Keycode.UP_ARROW)
        if not bt2.value:
            led.value = 1
            kbd.send(Keycode.DOWN_ARROW)
        if not bt3.value:
            led.value = 0
            kbd.send(Keycode.ENTER)
        if not bt4.value:
            led.value = 1
            kbd.send(Keycode.ENTER)


def loopPi():
    while True:
        time.sleep(loopSec)
        if not bt1.value:
            led.value = 0
            kbd.send(Keycode.CONTROL, Keycode.C)
        if not bt2.value:
            stringTokey(kbd,"pkill -f ffmpeg\r",FIX_Waiting,0.01)
            led.value = 1
        if not bt3.value:
            led.value = 0
            stringTokey(kbd, "sudo node index.js\r", FIX_Waiting, 0.01)
        if not bt4.value:
            led.value = 1
            stringTokey(kbd, "cd github/ocr/pi/\r", FIX_Waiting, 0.01)
