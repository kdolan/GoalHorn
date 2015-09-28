#!/bin/bash
echo 4 > /sys/class/gpio/export #Setup 4 as GPIO
echo in > /sys/class/gpio/gpio4/direction #Set as input for button

echo 17 > /sys/class/gpio/export #Setup 17 as GPIO
echo out > /sys/class/gpio/gpio17/direction
echo 1 > /sys/class/gpio/gpio17/value #Set starting value HIGH (active low control)

echo 27 > /sys/class/gpio/export #Setup 27 as GPIO
echo in > /sys/class/gpio/gpio17/direction #Set as input for key (enable)

