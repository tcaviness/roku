
from roku import Roku
import configparser as config
from gpiozero import LED
from signal import pause


def main():
    devices = Roku.discover(timeout=15, retries=3)
    ledB = LED(27)
    if not devices:
        ledB.on()
        print("empty")
        pause()
    else:
        ips=str()
        for device in devices:
            print(device.host)
            ips=device.host
            configs = config.ConfigParser()
            configs.read('config.ini')
            configs.set('tv_ips','ip',ips)
            with open('config.ini','w') as cfile:
                configs.write(cfile)
            if len(devices) > 2:
              ledB.blink(on_time=0.5, off_time=0.5)
              pause()
            else:
              ledB.blink()
              pause()

if __name__ == "__main__":
    main()
