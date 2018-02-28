#!/usr/bin/env python

class Temperature:
    def __init__(self, sensorAddress):
        self.sensorAddress = sensorAddress

    def rawValue(self):
        sensor = open(self.sensorAddress)
        value = sensor.read()
        sensor.close()
        return value

    def read(self):
        temperatureData = self.rawValue().split("\n")[1].split(" ")[9]
        value = float(temperatureData[2:]) / 1000
        return value
