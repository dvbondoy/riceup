import RPi.GPIO as GPIO
import time
import configparser
from helpers import csvlog

pwmPin = 16
ct = time.time()

config = configparser.ConfigParser()
config.read('config.ini')

intensity = config['VIBRATION']['intensity']
duration = config['VIBRATION']['duration']

global pwm
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.output(pwmPin, GPIO.LOW)
pwm = GPIO.PWM(pwmPin, 1000)
pwm.start(0)

def destroy():
    pwm.stop()
    GPIO.output(pwmPin, GPIO.LOW)
    GPIO.cleanup()

def vibrate():
    pwm.ChangeDutyCycle(intensity)
    time.sleep(duration*60)
    destroy() #end vibrate

    #csv log
    csvlog.write_csv('motor',ct)
