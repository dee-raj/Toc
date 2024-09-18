def q0(s,i):
    print("q0->",end="")
    if (i==len(s)):
        print(s,"is divisible by 3")
        return
    if (s[i]=='0' or s[i]=='3' or s[i]=='6' or s[i]=='9'):
        q0(s,i+1)
    elif(s[i]=='1' or s[i]=='4' or s[i]=='7'):
        q1(s,i+1)
    else:
        q2(s,i+1)
def q1(s,i):
    print("q1->",end="")
    if (i==len(s)):
        print(s,"is not divisible by 3")
        return
    if (s[i]=='0' or s[i]=='3' or s[i]=='6' or s[i]=='9'):
        q1(s,i+1)
    elif(s[i]=='1' or s[i]=='4' or s[i]=='7'):
        q2(s,i+1)
    else:
        q0(s,i+1)
def q2(s,i):
    print("q2->",end="")
    if (i==len(s)):
        print(s,"is not divisible by 3")
        return
    if (s[i]=='0' or s[i]=='3' or s[i]=='6' or s[i]=='9'):
        q2(s,i+1)
    elif(s[i]=='1' or s[i]=='4' or s[i]=='7'):
        q0(s,i+1)
    else:
        q1(s,i+1)
s="423"
q0(s,0)
