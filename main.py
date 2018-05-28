#import RPi.GPIO as GPIO
import time


#channel = 21
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(channel, GPIO.OUT)

def device_on(pin)
    #GPIO.output(pin, GPIO.HIGH) # turn pump on
    print("GPIO pin {} set to HIGH (1)".format(pin))
    return

def device_off(pin):
    #GPIO.output(pin, GPIO.LOW)
    print("GPIO pin {} set to LOW (0)".format(pin))

if __name__ == '__main__':
    try:
        read
