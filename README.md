Roku Project


This is a project that the problem was I need to turn three tv's off and on at the same time. 
any computer that runs python can do this if it has Wi-Fi connection. To make it seem like all 
of them are turn off and on at the same time. I went with threads because, it would prosses it in seconds. 

What takes the longs time is doing the device lookup. It got put in its own service to run as a standalone app. 


Device Lookup Code:
<code>
 devices = Roku.discover(timeout=15, retries=3)
    ledB = LED(27)
    if not devices:
        ledB.blink()
        logging.info("empty")
        pause()
    else:
        ledB.on()
        for device in devices:
            logging.info(f'devices:'{device.host})
            ips = device.host
            config = config.configPariser()
            config.set('tvs_ips','ip', ips )
            with open('config.ini, w') as cfile:
                config.write(cfile)
            if devices > 2:
            ledb.blink(on_time=0.5, off_time=0.5)
            pause()
            </code>

Button Code: 
   <code>
   def turn_onoff(ip, bool):
 try:
    roku = Roku(ip)

        if bool = True:
            roku.poweron()
        if bool = False:
            roku.poweroff()
 except Exception as Error:
        logging.INFO(f"Failed to connect to {ip}. Error:{Error}")

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
       
 def button():

 button.when_pressed = main()
 button.when_held = restart()
 pause()

if __name__ == "__main__":
    logging.basicConfig(filename='gpio.log', level=logging.INFO)
    button()    

   <code>
