import threading
import math
import time
def cube():
    for n in range(0,6):
        print(n*n*n,"is the cube",n)
        time.sleep(0.2)
def cuberoot():
    cube=0
    for i in range(1,6):
        cube1=math.pow(i,1/3)
        print("cuberoot of ",i*i*i,"is ", i)
        time.sleep(0.2)
print("multithreading")
t1=threading.Thread(name="cube",target=cube)
t2=threading.Thread(name="cuberoot",target=cuberoot)
t1.start()
t1.join()
t2.start()
t2.join()

