import os
import os.path

import mss
import time

with mss.mss() as sct:
    for x in range(300):
        filename = sct.shot(output="test/mon-"+str(x)+".png")
        print(filename)
        time.sleep(10)

import serial
ser = serial.Serial('com20')  # open serial port
print(ser.name)         # check which port was really used
line = ser.readline()
print(line)

ser.write(b'hello')     # write a string2935167479
ser.close()             # close portd52180362