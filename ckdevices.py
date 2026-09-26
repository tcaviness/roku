from roku import Roku
import configparser as config 
from gpiozero import LED
from signal import pause
import logging as log

logging = log.getLogger(__name__)

def main():
    #logging.basicConfig(filename='device.log', level=logging.INFO)
    devices = Roku.discover(timeout=15, retries=3)
    ledB = LED(27)
    if not devices:
        ledB.blink()
        logging.info("empty")
        pause()
    else:
        ledB.on()
        for device in devices:
            logging.info(f'devices:{device.host}')
            ips = device.host
            config = config.configPariser()
            config.set('tvs_ips','ip', ips )
            with open('config.ini','w') as cfile:
                config.write(cfile)
            if devices > 2:
            ledb.blink(on_time=0.5, off_time=0.5)
            pause()

if __name__ == "__main__":
    main()
