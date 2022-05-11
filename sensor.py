#!/usr/bin/python3

"""
Get temperature and humidity with aht20
Author:caling/jun
"""

import time
import board
import adafruit_ahtx0
#import schedule

i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

#depricated
def sense():
    #return {"temp":sensor.temperature,"hmdt":sensor.relative_humidity}
    f = open('/home/pi/riceup/temperature.txt','a')
    f.write(str(sensor.temperature)+','+str(sensor.relative_humidity)+'\n')
    f.close()

#Get temperature and humidity
#Return a dictionary
def get_temp():
    return {"temp":sensor.temperature, "hum":sensor.relative_humidity}

#schedule.every().minute.do(sense)

#if __name__ == '__main__':
#    sense()
#    while True:
#        schedule.run_pending()
#        time.sleep(1)
