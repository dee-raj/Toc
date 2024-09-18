#program do design DFA that accepts string of input E={0,1} ending with 01 or 10
def q0(state,inStr):
    print("Q0=> ",end='')
    if inStr==len(state):
        print("\nNot a final state......so the input string will not accept.")
        return
    if state[inStr]=='0':
        q1(state,inStr+1)
    else:
        q2(state,inStr+1)

def q1(state,inStr):
    print("Q1=> ",end='')
    if inStr==len(state):
        print("\nNot a final state......so the input string will not accept.")
        return
    if state[inStr]=='0':
        q1(state,inStr+1)
    else:
        q3(state,inStr+1)

def q2(state,inStr):
    print("Q2=> ",end='')
    if inStr==len(state):
        print("\nNot a final state......so the input string will not accept.")
        return
    if state[inStr]=='0':
        q4(state,inStr+1)
    else:
        q2(state,inStr+1)

def q3(state,inStr):
    print("Q3=> ",end='')
    if inStr==len(state):
        print("\nIts a final state......so the input string will accept.")
        return
    if state[inStr]=='0':
        q4(state,inStr+1)
    else:
        q2(state,inStr+1)

def q4(state,inStr):
    print("Q4=> ",end='')
    if inStr==len(state):
        print("\nIts a final state......so the input string will accept.")
        return
    if state[inStr]=='0':
        q1(state,inStr+1)
    else:
        q3(state,inStr+1)
#main
string_W="1010010"
print(f"State transition for {string_W} are:")
q0(string_W,0)