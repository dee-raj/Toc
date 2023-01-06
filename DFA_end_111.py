# program to design a DFA to accept consucative 111

def A(s,i): #start state
    print("A-> ",end='')
    if i==len(s):
        print("not a final state")
        return
    if s[i]=='1':
        B(s,i+1)
    else:
        A(s,i+1)


def B(s,i):
    print("B-> ",end='')
    if i==len(s):
        print("not a final state")
        return
    if s[i]=='1':
        C(s,i+1)
    else:
        A(s,i+1)


def C(s,i):
    print("C-> ",end='')
    if i==len(s):
        print("not a final state")
        return
    if s[i]=='1':
        D(s,i+1)
    else:
        A(s,i+1)


def D(s,i): #final state
    print("D-> ",end='')
    if i==len(s):
        print("Its a final state")
        return
    if s[i]=='1':
        D(s,i+1)
    else:
        A(s,i+1)
# w="10110111"
w="1011"
print(f"for the string '{w}' Transition states are:")
A(w,1)