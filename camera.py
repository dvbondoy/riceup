from picamera import PiCamera
from time import sleep
import configparser
from helpers import csvlog

config = configparser.ConfigParser()
config.read('config.ini')
path = config["CAMERA"]["path"]
duration = config["CAMERA"]["duration"]
ct = time.time()

camera = PiCamera()

def capture_vid():
    #camera.start_preview()
    #log it first
    csvlog.write_csv('camera', ct)

    camera.start_recording(config['CAMERA']['path']+ str(ct) + '-video.h264')
    sleep(duration)
    camera.stop_recording()
    #camera.stop_preview()
