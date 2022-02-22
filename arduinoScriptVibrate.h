#!/bin/bash
/home/farouq/arduino-1.8.19/hardware/tools/avr/bin/avrdude -C/home/farouq/arduino-1.8.19/hardware/tools/avr/etc/avrdude.conf -v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D -Uflash:w:/tmp/arduino_build_805148/Vibration.ino.hex:i
