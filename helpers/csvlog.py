import csv
import configparser
import aht
import time
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

path = config['CSV']['path']
#ct = datetime.fromtimestamp(time.time())#current time
data = aht.sense()#temp and hum

def write_csv(logtype, ct):
    try:
        f = open(path,'a')
        writer = csv.writer(f)

        if(logtype == 'mic'):
            row = [datetime.fromtimestamp(ct), str(ct)+'-recording.wav',\
            '{0:.2f}'.format(data["temp"]), '{0:.2f}'.format(data["hum"])]
        elif(logtype == 'camera'):
            row = [datetime.fromtimestamp(ct), str(ct) + '-video.h264']
        elif(logtype == 'motor'):
            row = [datetime.fromtimestamp(ct),'vibration activated']
        elif(logtype == 'fan'):
            row = [datetime.fromtimestamp(ct),'fan activated']
        else:
            row = [datetime.fromtimestamp(ct),logtype]

        writer.writerow(row)
        f.close()
    except Exception as e:
        logs.write_logs(e)
