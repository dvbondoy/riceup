"""
Script for recording sound from mems mic
author:caling/jun
"""
import os
import time
from datetime import datetime
from helpers import logs
import board
from helpers import csvlog
import adafruit_ahtx0
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

def record():
    #current timestamp
    ct = time.time()
    #temperature
    temp = sensor.temperature
    #humidity
    hum = sensor.relative_humidity

    #record now
    try:
        os.system('arecord -d ' + config['RECORDING']['duration'] +\
        ' -D dmic_sv -c2 -r 48000 -f S32_LE -t wav -V mono -v '\
        + config['RECORDING']['path'] + str(ct) + '-recording.wav')
    except Exception as e:
        logs.write_log(e)

    #csv log
    csvlog.write_csv()

    #log
    # logging.info('Record End: %s', datetime.now())
    # logging.info('File : %s-recording.wav, Temperature: %s, Humidity: %s', ct, temp, hum)
    # print('log saved...')
