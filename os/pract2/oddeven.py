import threading
from time import sleep
def print_thread(x):
    if x%2==0:
        even(x)
    else:
        odd(x)
    sleep(1)
def even(y):
    print(y," is even" )
def odd(y):
    print(y," is odd")
thread_list=[]
thread_even=[]
thread_odd=[]
for i in range(1,11):
    t=threading.Thread(target=print_thread(i))
    thread_even.append(t)
for thread in thread_list:
    thread.start()
    thread.join()
