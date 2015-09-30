import time
import sys
import os
import urllib2
from hardware_interface import *

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

if __name__ == "__main__":
	#INIT
    horn_file = DEFAULT_HORN
    software_only = False
    #deactivate_goal_light()
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
        #Poll GPIO
        button = read_gpio(GPIO_GOAL_BUTTON)
        key = read_gpio(GPIO_KEY)
        #Check for software trigger
        softwareTrigger = os.path.isfile(TRIGGER_PATH)
        if((button and key) and not software_only): #pressed and enabled
            print("GOAL!! - Hardware")
            urllib2.urlopen("http://localhost/goal/"+horn_file+"?source=hardware").read() #goal(horn_file)
        elif(button):
            print("Button - Key Disabled")
            time.sleep(0.1) #Wait before checking input again
        elif(softwareTrigger):
            print("GOAL!! - Software")
            os.remove(TRIGGER_PATH) #Remove trigger file
            urllib2.urlopen("http://localhost/goal/"+horn_file+"?source=hardware").read() #goal(horn_file)    
