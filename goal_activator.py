import subprocess
import time
import constants
import RPi.GPIO as GPIO
import hardware_monitor #for GPIO Setup function
#The set-up GPIO function must be called for all scripts using GPIO


hardware_monitor.setup_gpio() #Setup GPIO

def deactivate_goal_light():
    GPIO.output(constants.GPIO_GOAL_LIGHT, 1) #Turn off goal light

def goal(path):
    print(path)
    GPIO.output(constants.GPIO_GOAL_LIGHT, 0) #Turn on goal light
    print("GOAL!!!")
    time.sleep(0.25)
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(11.75)
    GPIO.output(constants.GPIO_GOAL_LIGHT, 1) #Turn off goal light
    print(constants.READY_STRING)

def penalty(path):
    print("Penalty! B-O-X!")
    GPIO.output(constants.GPIO_GOAL_LIGHT, 0) #Turn on goal light
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(8.5)
    GPIO.output(constants.GPIO_GOAL_LIGHT, 1) #Turn off goal light
    print(constants.READY_STRING)