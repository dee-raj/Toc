#program to design a machine for accepting same start and end symbols of (1,0)
def q0(w='',index=0):
    print("Q0=> ",end='')
    if index== len(w):
        print("\njust started and need a symbol to run the machine.")
        return
    if w[index]=='0':
        q1(w,index +1)
    else:
        q3(w,index +1)

def q1(w='',index=0):
    print("Q1=> ",end='')
    if index== len(w):
        print("\nA accepting state, string is start and end with same symbol")
        return
    if w[index]=='0':
        q1(w,index +1)
    else:
        q2(w,index +1)

def q2(w='',index=0):
    print("Q2=> ",end='')
    if index== len(w):
        print("\nIts not a final state, string is start and end with same symbol.")
    if w[index]== '0':
        q1(w,index +1)
    else:
        q2(w,index +1)

def q3(w='',index=0):
    print("Q3=> ",end='')
    if index== len(w):
        print("\nA accepting state, string is start and end with same symbol")
        return
    if w[index]=='0':
        q4(w,index +1)
    else:
        q3(w,index +1)

def q4(w='',index=0):
    print("Q4=> ",end='')
    if index== len(w):
        print("\nIts not a final state, string is start and end with same symbol.")
    if w[index]== '0':
        q4(w,index +1)
    else:
        q3(w,index +1)
#main
w='101101'
# w=''
print(f"Is [{w}] start and end with same symbol...see transition states.")
q0(w)


"""
Output

Is [101101] start and end with same symbol...see transition states.
Q0=> Q3=> Q4=> Q3=> Q3=> Q4=> Q3=> 
A accepting state, string is start and end with same symbol

Is [] start and end with same symbol...see transition states.
Q0=>
just started and need a symbol to run the machine.

"""