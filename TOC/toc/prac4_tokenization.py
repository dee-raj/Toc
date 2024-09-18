stack1=[]
stack2=[]
def A(s,i=0):
    if i == len(s):
        print("")
        return
    if s[i] == 'a':
        stack1.append(s[i])
        stack2.append(s[i])
        #print(stack1)
        A(s,i+1)
    if s[i] == '$':
        B(s,i+1)
    else:
        A(s,i+1)
def B(s,i):
    #print(stack1)
    if i == len(s):
        print("NO")
        return
    if s[i+1] == 'b':
        stack1.pop()
        B(s,i+1)
    elif s[i] == '&':
        C(s,i+1)
    else:
        B(s,i+1)
def C(s,i):
    if i == len(s):
        D(s)
        return
    print(stack2)
    if s[i] == 'c':
        stack2.pop()
        C(s,i+1)
    else:
        D(s)
def D(s):
    if len(stack1) and len(stack2) == 0:
        print("Accepted")
    else:
        print("NOT ACCEPt")
A('a$b&c')