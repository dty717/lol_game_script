from _init import kbd,mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import time

def ZED_escape():
    kbd.send(Keycode.W)
    time.sleep(0.01)
    kbd.send(Keycode.W)
    mouse.click(Mouse.RIGHT_BUTTON)
    return 1

global test
test = 0.1

def ZED_R_with_escape():
    global test
    mouse.move(380,480)
    kbd.send(Keycode.W)
    time.sleep(0.1)
    mouse.move(-380,-480)
    kbd.send(Keycode.R)
    test += 0.1
    time.sleep(1.4)
    print(test)
    kbd.send(Keycode.E)
    time.sleep(0.2)
    kbd.send(Keycode.Q)
    time.sleep(test)
    kbd.send(Keycode.W)
    time.sleep(0.1)
    mouse.move(620,620)
    time.sleep(0.2)
    mouse.click(Mouse.RIGHT_BUTTON)
    return 1

def mouseMove1():
    mouse.move(-50,-50)
    return 1

def mouseMove2():
    mouse.move(50,50)
    return 1
