def A(s,i):
    print('A->',end="")
    if(i==len(s)):
        print('No')
        return
    if s[i]=='a':
        B(s,i+1)
    else:
        D(s,i+1)

def B(s,i):
    print('B->',end="")
    if(i==len(s)):
        print('No')
        return
    if s[i]=='a':
        B(s,i+1)
    else:
        C(s,i+1)

def C(s,i):
    print('C->',end="")
    if(i==len(s)):
        print('No')
        return
    if s[i]=='a':
        B(s,i+1)
    else:
        C(s,i+1)

def D(s,i):
    print('D->',end="")
    if(i==len(s)):
        print('No')
        return
    if s[i]=='a':
        B(s,i+1)
    else:
        D(s,i+1)

def E(s,i):
    print('E->',end="")
    if(i==len(s)):
        print('No')
        return
    if s[i]=='a':
        D(s,i+1)
    else:
        E(s,i+1)

#main
s='aababba'
print(s)
A(s,0)
