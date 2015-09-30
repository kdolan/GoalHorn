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
    gpio.write(str(value))
    gpio.close()