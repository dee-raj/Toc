stack=[]
a0=0
def A(s,i=0):
    global a0
    print("=>A ",end='')
    if i==len(s):
        print("NO")
        return
    stack.append(s[i])
    if s[i+1] =='1':
        B(s,i+1)
    else:
        a0+=1
        A(s,i+1)
def B(s,i):
    global  a0
    print("=>B ",end='')
    if i==len(s):
        print("NO")
        return
    if s[i-a0-1]=='0':
        stack.pop()
        B(s,i+1)
    else:
        C(s)

def C(s):
    print("=>C ",end='')
    if len(stack)==0:
        print("accept")
    else:
        print("not")
        print(stack)
A('0001111111111111111111111111000')