import subprocess
import time
import sys
import os

DEFAULT_HORN = "/horns/rit_horn_short_band.wav"
TRIGGER_PATH = "/horns/scripts/GOAL.trigger"
READY_STRING = "Waiting for a goal..."

def write_light_value(value):
    light = open("/sys/class/gpio/gpio17/value", "w")
    light.write(value)
    light.close()

def goal(path):
    write_light_value("0")
    print("GOAL!!!")
    time.sleep(0.25)
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(11.75)
    write_light_value("1")
    print(READY_STRING)

if __name__ == "__main__":
    #subprocess.call("./setup_gpio.sh")
    horn_file = DEFAULT_HORN
    software_only = False
    if(len(sys.argv) == 2):
        horn_file = sys.argv[1]
    if(len(sys.argv) == 3): #path and software only
        horn_file = sys.argv[1]
        software_only = True
        READY_STRING += " (Software Trigger Only)"
    print(READY_STRING)
    write_light_value("1")
    while True:
        #Poll GPIO
        f_gpio = open("/sys/class/gpio/gpio4/value", "r")
        text = f_gpio.read()[0]
        f_gpio.close()
        #Check for software trigger
        softwareTrigger = os.path.isfile(TRIGGER_PATH)
        if(text == "1" and not software_only): #pressed
            goal(horn_file)
            #os.remove(TRIGGER_PATH) #Do not trigger duplicate
        elif(softwareTrigger):
            os.remove(TRIGGER_PATH) #Remove trigger file
            goal(horn_file)
            
