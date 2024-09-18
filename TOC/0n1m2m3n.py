stack=[]
def A(s,i=0):
    print("=>A ",end='')
    if i==len(s):
        print("The string has only 0 or empty.")
        return
    stack.append(s[i])
    if s[i+1]=='0':
        A(s,i+1)
    elif s[i+1]=='1':
        B(s,i+1)

def B(s,i):
    print("=>B ",end='')
    if i==len(s):
        print("The string has only 0 and 1.")
        return
    stack.append(s[i])
    if s[i+1]=='2':
        C(s,i+1)
    elif s[i+1]=='1':
        B(s,i+1)
def C(s,i):
    print("=>C ",end='')
    if i==len(s):
        print("The string does not have 3.")
        return
    if s[i]=='2':
        stack.pop()
    if s[i+1]=='3':
        D(s,i+1)
    else:
        C(s,i+1)
def D(s,i):
    print("=>D ",end='')
    if s[i]=='3':
        stack.pop()
        D(s,i+1)
    if s[i]=='#':
        E(s,i)

def E(s,i):
    print("=>E ",end='')
    # print(s[i],stack,i)
    if len(stack)==0:
        print(f"\nThe string {s} is in form 0n1m2m30.")
    else:
        print(f"\nThe string {s} is NOT in form 0n1m2m30.")
A('0123#')
print('\n')
A('001233#')
# print('\n')
# A('011223#')
# print('\n')
# A('00112233#')
# print('\n')
# A('01123#')