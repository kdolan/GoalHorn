import time
import sys
import os
import urllib2
import hardware_interface

DEFAULT_HORN = "rit_horn_short_band.wav"
TRIGGER_PATH = "/horns/scripts/GOAL.trigger"
READY_STRING = "Waiting for a goal..."

"""
GPIO Summary:
GPIO 4: Button Input
GPIO 27: Key Input
GPIO 17: Goal light (Active Low) 
"""

GPIO_GOAL_BUTTON = 4
GPIO_KEY = 27
	
"""
Returns int value of GPIO.
1 for high
0 for low

Input pin: int or string for pin to read
"""
def read_gpio(pin):
	gpio = open("/sys/class/gpio/gpio" + str(pin) + "/value", "r")
	text = gpio.read()[0]
	gpio.close()
	return int(text)

"""
Write the value to the pin.
Both value and pin should be ints
"""
def write_gpio(pin, value):
	gpio = open("/sys/class/gpio/gpio" + str(pin) + "/value", "w")
    gpio.write(value)
    gpio.close()

if __name__ == "__main__":
	#INIT
    horn_file = DEFAULT_HORN
    software_only = False
	hardware_interface.write_gpio(GPIO_GOAL_LIGHT, 1) #Set Goal Light to Off
    if(len(sys.argv) == 2):
        horn_file = sys.argv[1]
    if(len(sys.argv) == 3): #path and software only
        horn_file = sys.argv[1]
        software_only = True
        READY_STRING += " (Software Trigger Only)"
	
	#init local vars
	button = 0
	key = read_gpio(GPIO_KEY)
	#END INIT
    print(READY_STRING)
	
    while True: 
        "#Poll GPIO
		button = read_gpio(GPIO_GOAL_BUTTON)
		key = read_gpio(GPIO_KEY)
        #Check for software trigger
        softwareTrigger = os.path.isfile(TRIGGER_PATH)
        if((button and key) and not software_only): #pressed and enabled
            urllib2.urlopen("http://localhost/goal/"+horn_file).read() #goal(horn_file)
        elif(softwareTrigger):
            os.remove(TRIGGER_PATH) #Remove trigger file
            urllib2.urlopen("http://localhost/goal/"+horn_file).read() #goal(horn_file)    