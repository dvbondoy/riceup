#! /usr/bin/python3

import schedule
import mems
import vibrator
import fan
import light
#import camera
import sensor
import configparser
import time
import logging

logging.basicConfig(filename='/home/pi/riceup/logs/schedule.log', format='%(asctime)s %(message)s')
schedule_logger = logging.getLogger('schedule')
schedule_logger.setLevel(level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('/home/pi/riceup/config.ini')

schedule.every(int(config['MIC']['interval_hr'])).hours.at(':'+config['MIC']['begin_at']).do(mems.record)

if(config['DEVICES']['vibrator'] == 'on'):
    interval = int(config['MOTOR']['interval_hr'])
    intensity =  int(config['MOTOR']['intensity'])
    schedule.every(interval).hours.at(':'+config['MOTOR']['begin_at']).do(vibrator.vibrate_on,intensity=intensity)
    schedule.every(interval).hours.at(':'+config['MOTOR']['end_at']).do(vibrator.vibrate_off)

if(config['DEVICES']['fan'] == 'on'):
    schedule.every(int(config['FAN']['interval_hr'])).hours.at(':'+config['FAN']['begin_at']).do(fan.fan_on)
    schedule.every(int(config['FAN']['interval_hr'])).hours.at(':'+config['FAN']['end_at']).do(fan.fan_off)

if(config['DEVICES']['light'] == 'on'):
    schedule.every(int(config['LIGHT']['interval_hr'])).hours.at(':'+config['LIGHT']['begin_at']).do(light.on)
    schedule.every(int(config['LIGHT']['interval_hr'])).hours.at(':'+config['LIGHT']['end_at']).do(light.off)

if(config['DEVICES']['camera'] == 'on'):
    schedule.every(int(config['CAMERA']['interval_hr'])).hours.at(':'+config['CAMERA']['begin_at']).do(camera.capture_vid)
    schedule.every(int(config['CAMERA']['interval_hr'])).hours.at(':'+config['CAMERA']['end_at']).do(camera.capture_stop)

def get_jobs():
    all_jobs = schedule.get_jobs()
    print(all_jobs)

schedule.every(1).minutes.do(get_jobs)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
