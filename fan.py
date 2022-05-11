"""
WIRINGS

Raspberry to Relay:
    GPIO 24 ==> in
    5v ==> vcc
    Gnd ==> Gnd

Relay:
    NO ==> Fan positive(+)
    COM ==> PSU positive(+)

Fan:
    negative ==> PSU negative(-)

Author:caling/jun
"""
#import RPi.GPIO as GPIO
import gpiozero

#pin = 18
RELAY_FAN = 24

fan = gpiozero.OutputDevice(RELAY_FAN,active_high=False, initial_value=True)

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(pin, GPIO.OUT)

def fan_off():
    print('fan off')
    #GPIO.output(pin, GPIO.HIGH)
    fan.off()

def fan_on():
    print('fan on')
    #GPIO.output(pin, GPIO.LOW)
    fan.on()

fan_off()
