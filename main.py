from Lcd import Lcd
from Temperature import Temperature
from time import sleep, strftime
from datetime import datetime
import commands

DEVICE_ADDRESS = "28-00000244197d"
DEVICE_FILENAME = "/sys/bus/w1/devices/" + DEVICE_ADDRESS + "/w1_slave"

SERIAL_PORT = "/dev/ttyAMA0"
IP_ADDRESS = commands.getoutput("hostname -I").split(" ")[0]

TEMPERATURE_TEXT = "Temp: {0:.2f}"

lcd = Lcd(SERIAL_PORT)
temperature = Temperature(DEVICE_FILENAME);

if (lcd.isOpen()):
    showIp = True
    changes = 0
    text = TEMPERATURE_TEXT.format(temperature.read())
    while 1:
        lcd.clear()
        lcd.write(datetime.now().strftime("%d %b %H:%M:%S"))
        lcd.moveTo(1, 0)
        if  (changes == 5):
            changes = 0
            text = IP_ADDRESS if  showIp else TEMPERATURE_TEXT.format(temperature.read())
            showIp = not showIp

        lcd.write(text)
        changes += 1
        sleep(1.0)
