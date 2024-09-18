import RPi.GPIO as gp
from time import sleep
gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(14,gp.OUT)
gp.setup(19,gp.OUT)
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligble for voting.")
    gp.output(14,gp.HIGH)
    sleep(2)
    gp.output(14,gp.LOW)
else:
    print("You are NOT eligible for voting.")
    gp.output(19,gp.HIGH)
    sleep(3)
    gp.output(19,gp.LOW)



"""
import RPi.GPIO as gp
from time import sleep
gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(14,gp.OUT)
gp.setup(19,gp.OUT)
number=int(input("Enter a number: "))
if number%2==0:
    print("The number {} is even.".format(number))
    gp.output(14,gp.HIGH)
    sleep(2)
    gp.output(14,gp.LOW)
else:
    print("The number {} is odd.".format(number))
    gp.output(19,gp.HIGH)
    sleep(3)
    gp.output(19,gp.LOW)

"""