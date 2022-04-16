import logging
#from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

#logging.basicConfig(filename=config['LOG']['path'], level=logging.DEBUG)
try:
    logging.basicConfig(filename=config['LOG']['path'], level=logging.DEBUG,\
        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
except Exception as e:
    logging.info(e)

def write_log(message):
    logging.info(message)
