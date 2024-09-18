import RPi.GPIO as gp
from time import sleep
gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(27,gp.OUT)
pwm=gp.PWM(27,5)
pwm.start(0)
a=0
while a<3: #While True:
    for x in range(0,50):
        pwm.start(x)
        sleep(1)
    for x in range(0,50):
        pwm.start(50-x)
        sleep(2)
    a +=1
pwm.stop()
gp.cleanup()
