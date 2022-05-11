#! /usr/bin/python3

"""
Activate vibration module
Author:caling/jun
"""
#import RPi.GPIO as GPIO
import gpiozero 
import time

#pwmPin = 16
PIN = 23

vibrate = gpiozero.PWMOutputDevice(PIN, active_high=True, initial_value=False, frequency=100)

#global pwm
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pwmPin, GPIO.OUT)
#GPIO.output(pwmPin, GPIO.LOW)
#pwm = GPIO.PWM(pwmPin, 1000)
#pwm.start(0)

def vibrate_off():
    #pwm.stop()
    #GPIO.output(pwmPin, GPIO.LOW)
    #GPIO.cleanup()
    print('vibration off')
    vibrate.off()

def vibrate_on(intensity):
    print('vibration on')
    #pwm.ChangeDutyCycle(intensity) #change 0 to 100 for intensity
    vibrate.on()
