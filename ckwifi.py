from gpiozero import LED
import socket as soc
from signal import pause


def cecknet():
   ledR = LED(17)
   ledG = LED(18)

    IPaddress = soc.gethostbyname(soc.gethostbyname())
    if IPaddress == "127.0.0.1":
        ledR.on()
        return False
        pause()
    else:
        ledG.on()
        return True
        pause()

if __name__ == '__main__':
    ckcknet()
