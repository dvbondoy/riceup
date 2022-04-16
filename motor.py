import RPi.GPIO as GPIO
import time
from datetime import datetime
# import logging
import configparser

pwmPin = 16

parser = configparser.ConfigParser()
parser.read('config.ini')

intensity = parser[VIBRATION][intensity]
duration = parser[VIBRATION][duration]
csv_path = parser[CSV][path]

# def setup():
global pwm
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.output(pwmPin, GPIO.LOW)
pwm = GPIO.PWM(pwmPin, 1000)
pwm.start(0)

# logging.basicConfig(filename='/home/pi/logs.log', level=logging.DEBUG)

def destroy():
    pwm.stop()
    GPIO.output(pwmPin, GPIO.LOW)
    GPIO.cleanup()

def vibrate():
    ct = time.time()
    pwm.ChangeDutyCycle(intensity) #change 0 to 100 for intensity
    time.sleep(duration*60)  #vibrate in 10 secs, change to meet requirement
    destroy() #end vibrate

    #csv log
    f = open(csv_path,'a')
    writer = csv.writer(f)
    row = [datetime.fromtimestamp(ct),str(ct)+'-vibration']
    #str(temp).split('.',1)[0], str(hum).split('.',1)[0]]
    writer.writerow(row)
    f.close()

# if __name__ == '__main__':
#     setup()
#     try:
#         print("vibrating for N secs")
#         vibrate()
#         logging.info('Vibrate : '+str(time.time()))
#     except KeyboardInterrupt:
#         print("ending")
#         destroy()
