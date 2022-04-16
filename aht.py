"""
Get temperature and humidity with aht20
Author:caling/jun
Returns type of dictionary
"""

import time
import board
import adafruit_ahtx0
import logging

# Create sensor object, communicating over the board's default I2C bus
# uses board.SCL and board.SDA
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

def setup():
    logging.basicConfig(filename='/home/pi/logs.log', level=logging.DEBUG)
    
def sense():
    return {"temp":sensor.temperature,"hum":sensor.relative_humidity}

def main():
    setup()
    sense()

if __name__ == '__main__':
    main()
