# riceup
A research about rice bug detection.

## System Setup
1. Update raspberry pi  
`sudo apt update && sudo apt upgrade -y`

2. Install pip3 and camera  
`sudo apt install python3-pip -y`
`sudo apt-get install python-picamera python3-picamera`

3. Download and install raspi-blinka  
`wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py`  
`sudo python3 raspi-blinka.py`  

4. Download and install i2smic  
`wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2smic.py`  
`sudo python i2smic.py`  

5. Download riceup  
`git clone https://github.com/dvbondoy/riceup.git`  

6. Install requirements  
`cd riceup`  
`pip3 install -r requirements.txt`  

7. Configure settings in `config.ini` 
8. Run `python main.py` or `./main.py`

