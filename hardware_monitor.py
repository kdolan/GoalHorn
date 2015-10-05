import time
import sys
import os
import urllib2
import constants
import RPi.GPIO as GPIO

"""
GPIO Summary:
GPIO 4: Button Input
GPIO 27: Key Input
GPIO 17: Goal light (Active Low) 
"""

def setup_gpio():
    GPIO.setwarnings(False) #Disable Warnings
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(constants.GPIO_GOAL_LIGHT, GPIO.OUT)
    GPIO.setup(constants.GPIO_GOAL_BUTTON, GPIO.IN)
    GPIO.setup(constants.GPIO_KEY, GPIO.IN)
    
def deactivate_goal_light():
    GPIO.output(constants.GPIO_GOAL_LIGHT, 1)
    
if __name__ == "__main__":
    #INIT
    setup_gpio() #Init All GPIO
    deactivate_goal_light()
    horn_file = constants.DEFAULT_HORN
    software_only = False
    rdy_string = constants.READY_STRING
    if(len(sys.argv) == 2):
        horn_file = sys.argv[1]
    if(len(sys.argv) == 3): #path and software only
        horn_file = sys.argv[1]
        software_only = True
        rdy_string +=  " (Software Trigger Only)"
    
    #init local vars
    button = 0
    key = GPIO.input(constants.GPIO_KEY)
    #END INIT
    print(rdy_string)
    
    while True: 
        #Poll GPIO
        button = GPIO.input(constants.GPIO_GOAL_BUTTON)
        key = GPIO.input(constants.GPIO_KEY)
        if((button and key) and not software_only): #pressed and enabled
            print("GOAL!! - Hardware")
            urllib2.urlopen("http://localhost/goal/"+horn_file+"?source=hardware").read() #goal(horn_file)
        elif(button):
            print("Button - Key Disabled")
            time.sleep(0.1) #Wait before checking input again
