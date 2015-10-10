import subprocess
import time
import constants
import RPi.GPIO as GPIO
import urllib2
import hardware_monitor #for GPIO Setup function
#The set-up GPIO function must be called for all scripts using GPIO


hardware_monitor.setup_gpio() #Setup GPIO

def deactivate_goal_light():
    GPIO.output(constants.GPIO_GOAL_LIGHT, 1) #Turn off goal light

def goal(path, id):
    print(path)
    GPIO.output(constants.GPIO_GOAL_LIGHT, 0) #Turn on goal light
    print("GOAL!!!")
    time.sleep(0.25)
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(11.75)
    urllib2.urlopen("http://localhost/finish/"+str(id)+"?"+"source=localhost").read()
    print("Goal Finished")

def penalty(path, id):
    print("Penalty! B-O-X!")
    GPIO.output(constants.GPIO_GOAL_LIGHT, 0) #Turn on goal light
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(8.5)
    urllib2.urlopen("http://localhost/finish/"+str(id)+"?"+"source=localhost").read()
    print("Penalty Finished")