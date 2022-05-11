#!/usr/bin/python3

"""
Script for recording sound from mems mic
author:caling/jun
"""
import os
import time
from datetime import datetime
import csv
import configparser
import sensor

config = configparser.ConfigParser()
config.read('/home/pi/riceup/config.ini')

#record now
def record():
    #current time
    ct = time.time()
    path = config['MIC']['record_path']
    duration = int(config['MIC']['record_duration']) * 60 #record for 10 minutes=600 secs
    os.system('arecord -d ' + str(duration) +\
     ' -D dmic_sv -c2 -r 48000 -f S32_LE -t wav -V mono -v '\
     + path + str(ct) + '-recording.wav')

    data = sensor.get_temp()
    #csv log
#    temp = ''
#    with open('/home/pi/riceup/temperature.txt', 'r') as f:
        #get last line
#        temp = f.readlines()[-1]

    f = open(config['CSV']['csv_path'],'a')
    writer = csv.writer(f)
#    temp = temp.split(',')
#    row = [datetime.fromtimestamp(ct),str(ct)+'-recording.wav',\
#     '{0:.2f}'.format(float(temp[0])),'{0:.2f}'.format(float(temp[1]))]
    row = [datetime.fromtimestamp(ct),str(ct)+'-recording.wav',\
     '{0:.2f}'.format(data['temp']),'{0:.2f}'.format(data['hum'])]
    writer.writerow(row)
    f.close()
    return
