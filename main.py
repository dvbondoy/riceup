import time
import configparser
import schedule
import motor
import mic
import fan
import lights

config = configparser.ConfigParser()
config.read('config.ini')

if(config['MAIN']['recording'] == 'on'):
    schedule.every().hour.do(mic.record())
if(config['MAIN']['vibrate'] == 'on'):
    schedule.every().minute.at(':50').do(motor.vibrate())
if(config('MAIN']['blower'] == 'on'):
    schedule.every().minute.at(':50').do(fan.blow())
if(config['MAIN']['lights'] == 'on'):
    schedule.every().minute.at(':50').do(lights.toggle())

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
