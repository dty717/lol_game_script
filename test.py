import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import os
import board
import digitalio
import time

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# Type lowercase 'a'. Presses the 'a' key and releases it.

mouse = Mouse(usb_hid.devices)
mouse.move(-8000,-8000)

_x_ = 800
_y_ = 1060
x = _x_
y = _y_
_x = _x_
_y = _y_
mouse.move(x,y)
mouse.click(Mouse.LEFT_BUTTON)

_x_ = 1500
_y_ = 520
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_

mouse.move(x,y)
mouse.click(Mouse.LEFT_BUTTON)

kbd.send(Keycode.TWO)
kbd.send(Keycode.NINE)
kbd.send(Keycode.THREE)
kbd.send(Keycode.FIVE)
kbd.send(Keycode.ONE)
kbd.send(Keycode.SIX)
kbd.send(Keycode.SEVEN)
kbd.send(Keycode.FOUR)
kbd.send(Keycode.SEVEN)
kbd.send(Keycode.NINE)

_x_ = 1500
_y_ = 580
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_

mouse.move(x,y)
mouse.click(Mouse.LEFT_BUTTON)

kbd.send(Keycode.D)
kbd.send(Keycode.FIVE)
kbd.send(Keycode.TWO)
kbd.send(Keycode.ONE)
kbd.send(Keycode.EIGHT)
kbd.send(Keycode.ZERO)
kbd.send(Keycode.THREE)
kbd.send(Keycode.SIX)
kbd.send(Keycode.TWO)





mouse.move(-8000,-8000)

_x_ = 800
_y_ = 1060
x = _x_
y = _y_
_x = _x_
_y = _y_
mouse.move(x,y)
mouse.click(Mouse.LEFT_BUTTON)

seconds = 1
time.sleep(seconds)

_x_ = 450
_y_ = 200
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
mouse.click(Mouse.LEFT_BUTTON)

seconds = 1.5
time.sleep(seconds)


_x_ = 680
_y_ = 260
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
seconds = 1.5
time.sleep(seconds)
mouse.click(Mouse.LEFT_BUTTON)

seconds = 2
time.sleep(seconds)

_x_ = 850
_y_ = 850
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
mouse.click(Mouse.LEFT_BUTTON)

seconds = 2.5
time.sleep(seconds)
mouse.click(Mouse.LEFT_BUTTON)

_x_ = 1000
_y_ = 500
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
seconds = 12.5
time.sleep(seconds)
mouse.click(Mouse.LEFT_BUTTON)

_x_ = 960
_y_ = 770
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
seconds = 3.5
time.sleep(seconds)
mouse.click(Mouse.LEFT_BUTTON)






mouse.move(-8000,-8000)

_x_ = 860
_y_ = 1060
x = _x_
y = _y_
_x = _x_
_y = _y_
mouse.move(x,y)
mouse.click(Mouse.LEFT_BUTTON)

seconds = 1
time.sleep(seconds)

_x_ = 936
_y_ = 422
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
seconds = 0.2
time.sleep(seconds)
mouse.click(Mouse.RIGHT_BUTTON)
seconds = 0.2
time.sleep(seconds)
mouse.click(Mouse.RIGHT_BUTTON)
seconds = 0.2
time.sleep(seconds)
mouse.click(Mouse.RIGHT_BUTTON)
seconds = 0.2
time.sleep(seconds)
kbd.send(Keycode.Q)





mouse.move(-8000,-8000)

_x_ = 860
_y_ = 1060
x = _x_
y = _y_
_x = _x_
_y = _y_
mouse.move(x,y)
mouse.click(Mouse.LEFT_BUTTON)

seconds = 1
time.sleep(seconds)

mouse.move(-2800,-2800)
_x = 0
_y = 0
seconds = 1.2
time.sleep(seconds)
_x_ = 840
_y_ = 280
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
seconds = 0.2
time.sleep(seconds)
mouse.click(Mouse.LEFT_BUTTON)

_x_ = 525
_y_ = 577
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
seconds = 1.2
time.sleep(seconds)
mouse.click(Mouse.LEFT_BUTTON)

_x_ = 1000
_y_ = 840
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
seconds = 1
time.sleep(seconds)
mouse.click(Mouse.LEFT_BUTTON)

_x_ = 1200
_y_ = 206
x = _x_-_x
y = _y_ -_y
_x = _x_
_y = _y_
mouse.move(x,y)
seconds = 1
time.sleep(seconds)
mouse.click(Mouse.LEFT_BUTTON)





kbd.send(Keycode.A)

# Type capital 'A'.
kbd.send(Keycode.SHIFT, Keycode.A)

# Type control-x.
kbd.send(Keycode.CONTROL, Keycode.X)

# You can also control press and release actions separately.
kbd.press(Keycode.CONTROL, Keycode.X)
kbd.release_all()

# Press and hold the shifted '1' key to get '!' (exclamation mark).
kbd.press(Keycode.SHIFT, Keycode.ONE)
# Release the ONE key and send another report.
kbd.release(Keycode.ONE)
# Press shifted '2' to get '@'.
kbd.press(Keycode.TWO)
# Release all keys.
kbd.release_all()
