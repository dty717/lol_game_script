
import usb_hid
import board
import digitalio

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# Type lowercase 'a'. Presses the 'a' key and releases it.

mouse = Mouse(usb_hid.devices)


led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

bt1 = digitalio.DigitalInOut(board.GP14)
bt1.direction = digitalio.Direction.INPUT
bt1.pull = digitalio.Pull.UP
bt2 = digitalio.DigitalInOut(board.GP15)
bt2.direction = digitalio.Direction.INPUT
bt2.pull = digitalio.Pull.UP
bt3 = digitalio.DigitalInOut(board.GP16)
bt3.direction = digitalio.Direction.INPUT
bt3.pull = digitalio.Pull.UP
bt4 = digitalio.DigitalInOut(board.GP17)
bt4.direction = digitalio.Direction.INPUT
bt4.pull = digitalio.Pull.UP