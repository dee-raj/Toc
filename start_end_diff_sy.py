#program to design a machine that accepts a string which start and ends with different symbol over E={0,1}
def q0(str='',idx=0): #start state
    print("Q0=> ",end='')
    if idx==len(str):
        print("Initial state... string is required to run the machine.")
        return
    if str[idx]=='1':
        q1(str,idx +1)
    else:
        q2(str,idx +1)

def q1(str='',idx=0):
    print("Q1=> ",end='')
    if idx==len(str):
        print("string is not accepting by the machine.")
        return
    if str[idx]=='1':
        q5(str,idx +1)
    else:
        q3(str,idx +1)

def q2(str='',idx=0):
    print("Q2=> ",end='')
    if idx==len(str):
        print("string is not accepting by the machine.")
        return
    if str[idx]=='1':
        q4(str,idx +1)
    else:
        q5(str,idx +1)

def q5(str='',idx=0): #dead state all the inputss tarps here only
    print("Q5=> ",end='')
    if idx==len(str):
        print("It's a dead state machine will no longer responding for inputs.")
        return
    if str[idx]=='1':
        q5(str,idx +1)
    else:
        q5(str,idx +1)

def q3(str='',idx=0):
    print("Q3=> ",end='')
    if idx== len(str):
        print("Its a accepting state... given string will be accepted.")
        return 
    if str[idx]=='1':
        q1(str,idx +1)
    else:
        q3(str,idx +1)

def q4(str='',idx=0):
    print("Q4=> ",end='')
    if idx== len(str):
        print("Its a accepting state... given string will be accepted.")
        return 
    if str[idx]=='1':
        q4(str,idx +1)
    else:
        q2(str,idx +1)
#main
w='10001010'
# w='101'
print(f"is {w} start and end with diff symbols? to check transition states are:")
q0(w)

"""
OUTPUT

is 10001010 start and end with diff symbols? to check transition states are:
Q0=> Q1=> Q3=> Q3=> Q3=> Q1=> Q3=> Q1=> Q3=> Its a accepting state... given string will be accepted.

is 101 start and end with diff symbols? to check transition states are:
Q0=> Q1=> Q3=> Q1=> string is not accepting by the machine.

"""