from hardware_interface import *
import subprocess
import time
import constants
import RPi.GPIO as GPIO

"""
GPIO Summary:
GPIO 17: Goal light (Active Low) 
"""

def deactivate_goal_light():
    write_gpio(constants.GPIO_GOAL_LIGHT, 1) #Turn off goal light

def goal(path):
    print(path)
    write_gpio(constants.GPIO_GOAL_LIGHT, 0) #Turn on goal light
    print("GOAL!!!")
    time.sleep(0.25)
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(11.75)
    write_gpio(constants.GPIO_GOAL_LIGHT, 1) #Turn off goal light
    print(constants.READY_STRING)

def penalty(path):
    print("Penalty! B-O-X!")
    write_gpio(constants.GPIO_GOAL_LIGHT, 0) #Turn on goal light
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(8.5)
    write_gpio(constants.GPIO_GOAL_LIGHT, 1) #Turn off goal light
    print(constants.READY_STRING)