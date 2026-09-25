from gpiozero import LED
import socket
from signal import pause


def net():
   ledR = LED(17)
   ledG = LED(18)

IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        ledR.on()
        return False
        pause()
    else:
        ledG.on()
        return True
        pause()

if __name__ == '__main__':
      net()
