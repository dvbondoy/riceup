#import RPi.GPIO as GPIO
import gpiozero

#pin = 22
pin = 19

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pin, GPIO.OUT)

light = gpiozero.OutputDevice(pin, active_high=False, initial_value=True)

def on():
    print('on')
    #GPIO.output(pin, GPIO.LOW)
    light.on()

def off():
    print('off')
    #GPIO.output(pin, GPIO.HIGH)
    light.off()

#on()
