def q1(s,i):
    print("q1->",end=" ")
    if(i==len(s)):
        print("No")
        return;
    if(s[i]=='a'):
        q2(s,i+1)
    else:
        q4(s,i+1)
def q2(s,i):
    print("q2->",end=" ")
    if(i==len(s)):
        print("yes")
        return;
    if(s[i]=='a'):
        q2(s,i+1)
    else:
        q2(s,i+1)
def q0(s,i):
    print("qo->",end=" ")
    if(i==len(s)):
        print("No")
        return;
    if(s[i]=='a'):
        q1(s,i+1)
    else:
        q3(s,i+1)
def q3(s,i):
    print("q3->",end=" ")
    if(i==len(s)):
        print("Yes")
        return;
    if(s[i]=='a'):
        q4(s,i+1)
    else:
        q2(s,i+1)
def q4(s,i):
    print("q4->",end=" ")
    if(i==len(s)):
        print("No")
        return;
    if(s[i]=='a'):
        q4(s,i+1)
    else:
        q4(s,i+1)
#main
s="aaba"
print("state transition are:",end=" ")
q0(s,0)
