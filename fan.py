import RPi.GPIO as GPIO
import time

pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def fan_off():
    GPIO.output(pin, GPIO.HIGH)
    print('fan off')

def fan_on():
    GPIO.output(pin, GPIO.LOW)
    print('fan on')
