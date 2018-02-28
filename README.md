# temperature
Display temperature on LCD with raspberry pi

You need to active i2c and serial ports on raspberry (via $raspi-config). You need to add "dtoverlay=w1-gpio" to /boot/config.txt too.

```bash
$ sudo cp temperature.service /etc/systemd/system/temperature.service
$ sudo services temperature enable
```
