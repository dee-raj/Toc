import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(14,gp.OUT)
p=gp.PWM(14,5)
p.start(0)
input("Press return to stop")
sleep(5)
p.stop()
gp.cleanup()
