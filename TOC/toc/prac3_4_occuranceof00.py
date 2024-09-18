def A(s,i,o):
    print(" A",end="-> ")
    if i==len(s):
        print("\n number of occurence : ",o)
        return
    if s[i]=='0':
        B(s,i+1,o)
    else:
        A(s,i+1,o)
def B(s,i,o):
    print(" B",end="-> ")
    if i==len(s):
        print("\n number of occurence : ",o)
        return
    if s[i]=='0':
        C(s,i+1,o)
    else:
        A(s,i+1,o)
def C(s,i,o):
    o=o+1
    print(" C",end="-> ")
    if i==len(s):
        print("\n number of occurence : ",o)
        return
    if s[i]=='0':
        C(s,i+1,o)
    else:
        A(s,i+1,o)
s="100010000"
print(s)
A(s,0,0)