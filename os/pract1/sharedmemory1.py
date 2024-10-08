from threading import Thread
import time
import random
from queue import Queue
queue=Queue(10)
class producerThread(Thread):
    def run(self):
        nums=range(5)
        global queue
        while True:
            num=random.choice(nums)
            queue.put(num)
            print("Produced:",num)
            if num==4:
                break
            time.sleep(random.random())

class consThread(Thread):
    def run(self):
        global queue
        while True:
                num=queue.get()
                queue.task_done()
                print("Consumed:",num)
                time.sleep(random.random())
producerThread().start()
consThread().start()