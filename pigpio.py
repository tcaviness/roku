from roku import Roku
from gpiozero import Button
from signal import pause
import configparise as config
from concurrent.futures import ThreadPoolExecutor
import subprosses as sub
import logging as log

logging = log.getLogger(__name__)

button = Button(27,pullup=False,bounce_time=0.2,hold_time=5.0)

def turn_onoff(ip, bool):
 try:
    roku = Roku(ip)

        if bool = True:
            roku.poweron()
        if bool = False:
            roku.poweroff()
 except Exception as Error:
        logging.INFO(f"Failed to connect to {ip}. Error:{Error}")

def restart():
    sub.run("sudo", "restart")


def main():
    configs = config.Configering()
    configs.read('config.ini')
    devices = configs['tv_ips']['ip']
    press = False
    press not press
    with ThreadPoolExector(max_workers=len(devices)) as exector:
        results = exector.map(turn_onoff, devices, press)

    for result in results:
       logging.INFO(result)

    # threads=list()
    #
    # if devices >= 2:
    #     for device in devices:
    #         press = False
    #         press not press
    #         thread = td.Thread(target=turn_onoff, args=(device, press))
    #           threads.append(thread)
    #           thread.start()
    #           thread.join()


def button():

 button.when_pressed = main()
 button.when_held = restart()
 pause()

if __name__ == "__main__":
    logging.basicConfig(filename='gpio.log', level=logging.INFO)
    button()
