def A(s,i=0):
    print('A-> ',end='')
    if i==len(s):
        print("Input String can't be empty")
        return
    if s[i]=='1':
        C(s,i+1)
    else:
        B(s,i+1)

def B(s,i):
    print("B-> ",end='')
    if i==len(s):
        print("String is not ending with the same symbol of starting.")
        return
    if s[i]=='1':
        B(s,i+1)
    else:
        D(s,i+1)

def C(s,i):
    print("C-> ",end='')
    if i==len(s):
        print("String is not ending with the same symbol of starting.")
        return
    if s[i]=='0':
        C(s,i+1)
    else:
        E(s,i+1)

def D(s,i):
    print("D-> ",end='')
    if i==len(s):
        print(f"yes!, The string {s} is ending with same symbol of starting.")
        return
    if s[i]=='0':
        D(s,i+1)
    else:
        B(s,i+1)

def E(s,i):
    print("E-> ",end='')
    if i==len(s):
        print(f"yes!, The string {s} is ending with same symbol of starting.")
        return
    if s[i]=='1':
        E(s,i+1)
    else:
        C(s,i+1)
w='10001001011101'
A(w)