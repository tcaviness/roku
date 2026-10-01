from roku import Roku
from gpiozero import Button, LED
from signal import pause
import configparser as config
from concurrent.futures import ThreadPoolExecutor
import subprocess as sub
import logging as log

#logging = log.getLogger(__name__)
ledG = LED(17)
button = Button(22,pull_up=False,bounce_time=0.2,hold_time=5.0)
press = False

def turn_onoff(ips):
 ip, bool = ips
 
 try:
    roku = Roku(ip)
    print(f"{ip},{bool}")
    if bool==True:
      roku.poweron()
      return "on"
    if bool==False:
      roku.poweroff()
      return "off"
 except Exception as Error:
   print(f"Falied to connect to {ip}. Error:{Error}")
  # logging.INFO(f"Failed to connect to {ip}. Error:{Error}")

def restart():
    sub.run(["sudo", "reboot"])


def main():
    global press  
    configs = config.ConfigParser()
    configs.read('config.ini')
    devices = configs['tv_ips']['ip']

    press =not press
    listcom = []
    listcon = [[device, press] for device in devices.splitlines()]
    

    with ThreadPoolExecutor(max_workers=len(devices)) as exector:
        results = exector.map(turn_onoff, listcon) 

    for result in results:
       print(result)
      # logging.INFO(result)

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


def btn():
# logging.basicConfig(filename='button.log', level=logging.INFO)
 ledG.on()
 button.when_pressed = main
 button.when_held = restart
 pause()

if __name__ == "__main__":
    btn()
