from picamera import PiCamera
import time
import configparser
#from helpers import csvlog

config = configparser.ConfigParser()
config.read('config.ini')
path = config["CAMERA"]["vids_path"]
ct = time.time()

camera = PiCamera()

def capture_vid():
    #camera.start_preview()
    #csvlog.write_csv('camera', ct)
    camera.start_recording(path + str(ct) + '-video.h264')

def capture_stop():
    camera.stop_recording()
    #camera.stop_preview()
