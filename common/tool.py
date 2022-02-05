from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import time


NO_Waiting = 0
FIX_Waiting = 1
RAND_Waiting = 2


def handle_FIX_Waiting(keyboard, str, waitTime):
    for x in str:
        if x > '0' and x <= '9':
            keyboard.send(Keycode.ONE+int(x)-1)
        elif x == '0':
            keyboard.send(Keycode.ZERO)
        elif x >= 'a' and x <= 'z':
            keyboard.send(Keycode.A+ord(x)-ord('a'))
        elif x >= 'A' and x <= 'Z':
            keyboard.send(Keycode.A+ord(x)-ord('A'), Keycode.SHIFT)
        elif x == '\r':
            keyboard.send(Keycode.ENTER)
        elif x == '`':
            keyboard.send(Keycode.GRAVE_ACCENT)
        elif x == '-':
            keyboard.send(Keycode.MINUS)
        elif x == '=':
            keyboard.send(Keycode.EQUALS)
        elif x == '[':
            keyboard.send(Keycode.LEFT_BRACKET)
        elif x == ']':
            keyboard.send(Keycode.RIGHT_BRACKET)
        elif x == '\\':
            keyboard.send(Keycode.BACKSLASH)
        elif x == ';':
            keyboard.send(Keycode.SEMICOLON)
        elif x == '\'':
            keyboard.send(Keycode.QUOTE)
        elif x == ',':
            keyboard.send(Keycode.COMMA)
        elif x == '.':
            keyboard.send(Keycode.PERIOD)
        elif x == '/':
            keyboard.send(Keycode.FORWARD_SLASH)
        elif x == ' ':
            keyboard.send(Keycode.SPACE)
        elif x == '\t':
            keyboard.send(Keycode.TAB)
        elif x == '~':
            keyboard.send(Keycode.GRAVE_ACCENT, Keycode.SHIFT)
        elif x == '!':
            keyboard.send(Keycode.ONE, Keycode.SHIFT)
        elif x == '@':
            keyboard.send(Keycode.TWO, Keycode.SHIFT)
        elif x == '#':
            keyboard.send(Keycode.THREE, Keycode.SHIFT)
        elif x == '$':
            keyboard.send(Keycode.FOUR, Keycode.SHIFT)
        elif x == '%':
            keyboard.send(Keycode.FIVE, Keycode.SHIFT)
        elif x == '^':
            keyboard.send(Keycode.SIX, Keycode.SHIFT)
        elif x == '&':
            keyboard.send(Keycode.SEVEN, Keycode.SHIFT)
        elif x == '*':
            keyboard.send(Keycode.EIGHT, Keycode.SHIFT)
        elif x == '(':
            keyboard.send(Keycode.NINE, Keycode.SHIFT)
        elif x == ')':
            keyboard.send(Keycode.ZERO, Keycode.SHIFT)
        elif x == '_':
            keyboard.send(Keycode.MINUS, Keycode.SHIFT)
        elif x == '+':
            keyboard.send(Keycode.EQUALS, Keycode.SHIFT)
        elif x == '{':
            keyboard.send(Keycode.LEFT_BRACKET, Keycode.SHIFT)
        elif x == '}':
            keyboard.send(Keycode.RIGHT_BRACKET, Keycode.SHIFT)
        elif x == '|':
            keyboard.send(Keycode.BACKSLASH, Keycode.SHIFT)
        elif x == ':':
            keyboard.send(Keycode.SEMICOLON, Keycode.SHIFT)
        elif x == '"':
            keyboard.send(Keycode.QUOTE, Keycode.SHIFT)
        elif x == '<':
            keyboard.send(Keycode.COMMA, Keycode.SHIFT)
        elif x == '>':
            keyboard.send(Keycode.PERIOD, Keycode.SHIFT)
        elif x == '?':
            keyboard.send(Keycode.FORWARD_SLASH, Keycode.SHIFT)
        if waitTime:
            time.sleep(waitTime)
    return


def handle_NO_Waiting(keyboard, str):
    return handle_FIX_Waiting(keyboard, str)


def switch(x=NO_Waiting):
    return {
        NO_Waiting: handle_NO_Waiting,
        FIX_Waiting: handle_FIX_Waiting,
        RAND_Waiting: ""
    }.get(x, None)


def stringTokey(keyboard, str, waitType, waitParam):
    return switch(waitType)(keyboard, str, waitParam)
