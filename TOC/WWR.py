stack=[]
def q1(st,i=0):
    print("=>A ",end='')
    if i==len(st):
        print(f"\n[{st}] is Not in WWR form")
        return
    stack.append(st[i])
    if st[i+1] == '$':
        q2(st,i+1)
    else:
        q1(st,i+1)
def q2(st,i):
    print("=>B ",end='')
    if stack[len(stack)-1]==st[i]:
        stack.pop()
    if st[i+1]=="#":
        q3(st)
    else:
        try:
            q2(st,i+1)
        except IndexError:
            print("Index Error")
def q3(st):
    print("Accptance checking")
    if len(stack)==0:
        print(f"[{st}] is in WWR form")
    else:
        print(f"[{st}] is Not in WWR form")
s='shanti$inahs#'
print(f"State of transitions are: [{s}]")
q1(s)