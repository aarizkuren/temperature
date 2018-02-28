#!/usr/bin/env python
import serial

class Lcd:
    CLEAR = bytearray([254, 1])
    def __init__(self, serialPort):
        self.display = serial.Serial(serialPort, 9600, timeout = 0.1)

    def clear(self):
        self.write(self.CLEAR)

    def write(self, text):
        self.display.write(text)

    def moveTo(self, line, col):
        position = line * 192 + col
        cursor = bytearray([254, position])
        self.write(cursor)

    def isOpen(self):
        return self.display.isOpen()
