def q0(s,i):
    print("q0-->",end=" ")
    if(i==len(s)):
        print("No")
        return
    if(s[i]=='0'):
        q0(s,i+1)
    else:
        q1(s,i+1)


def q1(s,i):
    print("q1-->",end=" ")
    if(i==len(s)):
        print("No")
        return
    if(s[i]=='0'):
        q0(s,i+1)
    else:
        q2(s,i+1)


def q2(s,i):
    print("q2-->",end=" ")
    if(i==len(s)):
        print("No")
        return
    if(s[i]=='0'):
        q0(s,i+1)
    else:
        q3(s,i+1)


def q3(s,i):
    print("q3-->",end=" ")
    if(i==len(s)):
        print("No")
        return
    if(s[i]=='0'):
        q0(s,i+1)
    else:
        q3(s,i+1)

#main
s="010111"
print("State Trsnitions are:",end="")
q0(s,0)

        
