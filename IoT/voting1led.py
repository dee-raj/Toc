import RPi.GPIO as gp
from time import sleep
gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(21,gp.OUT)
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible for voing.")
    gp.output(21,gp.HIGH)
    sleep(1)
    gp.output(21,gp.LOW)
else:
    print("You are NOT eligible for voting.")