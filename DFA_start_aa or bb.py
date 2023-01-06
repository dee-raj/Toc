#program to degin DFA that accept string start with aa OR bb
def A(s,i):#start state
    print("A-> ",end='')
    if i==len(s):
        print("its a start state")
        return
    if s[i]=='a':
        B(s,i+1)
    elif s[i]=='b':
        C(s,i+1)
def B(s,i):
    print("B-> ",end='')
    if i==len(s):
        print("not a final state")
        return
    if s[i]=='a':
        E(s,i+1)
    else:
        D(s,i+1)
def C(s,i):
    print("C-> ",end='')
    if i==len(s):
        print("not a final state")
        return
    if s[i]=='a':
        D(s,i+1)
    else:
        E(s,i+1)
def D(s,i):#dead state
    print("D-> ",end='')
    if i==len(s):
        print("its a dead state")
        return
    if s[i]=='a':
        D(s,i+1)
    else:
        D(s,i+1)
def E(s,i):#final state
    print("E-> ",end='')
    if i==len(s):
        print("its a final state")
        return
    if s[i]=='a':
        E(s,i+1)
    else:
        E(s,i+1)
w='aababa'
w='bababab'
w='bbabab'
print(f"for input '{w}' transition states are:")
A('a',0)
