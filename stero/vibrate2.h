#!/bin/bash
/home/dongxinliang/arduino-1.8.19/hardware/tools/avr/bin/avrdude -C/home/dongxinliang/arduino-1.8.19/hardware/tools/avr/etc/avrdude.conf -v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D -Uflash:w:/home/dongxinliang/Vibrate2/Vibration2.ino.hex:i 
