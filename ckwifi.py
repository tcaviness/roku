from gpiozero import LED
import subprocess as sub
from signal import pause

ledR = LED(18)

def ckhost(): 
  result = sub.run(["hostname","-I"], capture_output=True, text=True)
  ip = result.stdout.strip()
  print(ip)
  if ip =="":
    ledR.on()
  else: 
    ledR.blink()


if __name__ == '__main__':
    ckhost()
    pause()
