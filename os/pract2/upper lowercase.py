import threading
from time import sleep
def print_thread(x):
        if x <= 90:
                upper(x)
        else:
                lower(x)
        sleep(0.2)
def upper(y):
        print("UPPER: ",chr(y))
def lower(y):
        print("LOWER:",chr(y))
thread_list = []
thread_upper = []
thread_lower = []
for i in range(65,269):
        t = threading.Thread(target = print_thread(i))
        if i <= 90:
                thread_upper.append(t)
for i in range(97,123):
        t = threading.Thread(target = print_thread(i))
        if i <= 122:
                thread_lower.append(t)
thread_list.extend(thread_upper)
thread_list.extend(thread_lower)
for thread in thread_list:
        thread.start()
        thread.join()
