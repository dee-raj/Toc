stack=[]
def A(s,i=0):
    print(" A",end="-> ")
    if i==len(s):
        print("Not Accepted")
        return
    stack.append(s[i])
    if s[i+1]=='$':
        B(s,i+1)
    else:
        A(s,i+1)
        
def B(s,i):
    print(" B",end="-> ")
    if i==len(s):
        print("Not Accepted")
        return
    l=len(stack)
    if stack[l-1]==s[i]:
        stack.pop()
        B(s,i+1)
    else:
        print("not accept")
    if s[i+1]=="#":
        C()   
        
def C():
    print(" C",end="-> ")
    if len(stack)==0:
        print("Accepted")
    else:
        print("not accepted")
        
s='shanti$itnahs#'
s='abc$cba#'
# s='abac$caba#'
print(s)
A(s)