#!/bin/bash
echo 4 > /sys/class/gpio/export #Setup 4 as GPIO
echo in > /sys/class/gpio/gpio4/direction

echo 17 > /sys/class/gpio/export #Setup 17 as GPIO
echo out > /sys/class/gpio/gpio17/direction
echo 1 > /sys/class/gpio/gpio17/value #Set starting value HIGH (active low control)
