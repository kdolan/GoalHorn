import subprocess
import time
import sys
import os

DEFAULT_HORN = "/horns/rit_horn_short_band.wav"
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
GPIO_GOAL_LIGHT = 17

def goal(path):
    write_gpio(GPIO_GOAL_LIGHT, 0) #Turn on goal light
    print("GOAL!!!")
    time.sleep(0.25)
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(11.75)
    write_gpio(GPIO_GOAL_LIGHT, 1) #Turn off goal light
    print(READY_STRING)

def penalty(path):
	print("Penalty! B-O-X!")
	write_gpio(GPIO_GOAL_LIGHT, 0) #Turn on goal light
	subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
	time.sleep(6)
	write_gpio(GPIO_GOAL_LIGHT, 1) #Turn off goal light
	print(READY_STRING)
	
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


def oldMain():
	#INIT
    horn_file = DEFAULT_HORN
    software_only = False
	write_gpio(GPIO_GOAL_LIGHT, 1) #Set Goal Light to Off
    if(len(sys.argv) == 2):
        horn_file = sys.argv[1]
    if(len(sys.argv) == 3): #path and software only
        horn_file = sys.argv[1]
        software_only = True
        READY_STRING += " (Software Trigger Only)"
	#END INIT
    print(READY_STRING)
    while True:
        #Poll GPIO
		button = read_gpio(GPIO_GOAL_BUTTON)
		key = read_gpio(GPIO_KEY)
        #Check for software trigger
        softwareTrigger = os.path.isfile(TRIGGER_PATH)
        if((button and key) and not software_only): #pressed and enabled
            goal(horn_file)
        elif(softwareTrigger):
            os.remove(TRIGGER_PATH) #Remove trigger file
            goal(horn_file)
