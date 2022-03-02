#!/bin/bash
/home/farouq/arduino-1.8.19/hardware/tools/avr/bin/avrdude -C/home/farouq/arduino-1.8.19/hardware/tools/avr/etc/avrdude.conf -v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D -Uflash:w:/home/farouq/OPC/Vib2/Vibrate_Two_One.ino.hex:i
