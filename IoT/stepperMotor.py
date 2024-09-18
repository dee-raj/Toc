import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BCM)
gp.setwarnings(False)
a=25
b=8
c=7
d=1
gp.setup(a,gp.OUT)
gp.setup(b,gp.OUT)
gp.setup(c,gp.OUT)
gp.setup(d,gp.OUT)

def setSteps(w1,w2,w3,w4):
    gp.output(a,w1)
    gp.output(b,w2)
    gp.output(c,w3)
    gp.output(d,w4)
    
def forward(delay,steps):
    for i in range(steps):
        setSteps(1,1,0,0)
        sleep(delay)

        setSteps(0,1,1,0)
        sleep(delay)

        setSteps(0,0,1,1)
        sleep(delay)

        setSteps(1,0,0,1)
        sleep(delay)

def backward(delay,steps):
    for i in range(steps):
        setSteps(0,0,1,1)
        sleep(delay)

        setSteps(0,1,1,0)
        sleep(delay)

        setSteps(1,1,0,0)
        sleep(delay)

        setSteps(1,0,0,1)
        sleep(delay)
        
while True:
    d=int(input("Enter delay time: "))
    s=int(input("How many steps: "))
    #forward(d,s)
    backward(d,s)
