import threading
from time import sleep
def print_thread(x):
    temp=x
    tot=0
    while(x>0):
        dig=x%10
        tot=tot*10+dig
        x=x//10
    if(temp==tot):
       palindrome(temp)
       sleep(1)
def print_thread2(x):
    temp=x
    tot=0
    while temp > 0 :
        digit = temp %10
        tot = tot + (digit**3)
        temp = temp//10
    if x == tot:
        armstrong(x)
        sleep(2)

def palindrome(y):
    print(y,"is palindromre number.")
def armstrong(y):
    print(y,"is armstrong number.")
thread_list=[]
#thread_palindrome=[]
thread_armstrong=[]
a=int(input("From: "))
b=int(input("To: "))
for i in range(a,b):
    t=threading.Thread(target=print_thread(i))
    t=threading.Thread(target=print_thread2(i))
for thread in thread_armstrong:
    thread.start()
    thread.join()
