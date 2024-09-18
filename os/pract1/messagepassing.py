from threading import Thread, Condition
import time
import random
queue=[]
max_num=10
cond=Condition()
class producerThread(Thread):
    def run(self):
        nums=range(5)
        global queue
        while True:
            cond.acquire()
            if len(queue)==max_num:
                print("queue is full Producer is waiting")
                cond.wait()
                print("Sapce in queue, consumer notified the producer")
                break
            num=random.choice(nums)
            queue.append(num)
            print("Produced:",num)
            cond.notify()
            cond.release()
            time.sleep(random.random())

class consThread(Thread):
    def run(self):
        global queue
        while True:
            cond.acquire()
            if not queue:
                print("Nothing is there is queue, consumer is waiting")
                cond.wait()
                print("produer added something and notified consumer")
                num=queue.pop()
                print("Consumed:",num)
                cond.notify()
                cond.release()
                time.sleep(random.random())

consThread().start()
producerThread().start()
