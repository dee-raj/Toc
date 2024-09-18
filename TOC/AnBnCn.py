#PDA for L={  AnBnCn where n>=1  }  aabbcc
stack=['$']
def q1(s,i=0):
    print("=>A ",end='')
    if i==len(s):
        print('Not accepted')
        return
    if s[i]=='a':
        stack.append(s[i])
        q1(s,i+1)
    if s[i]=='b' and stack[len(stack)-1]=='a':
        stack.pop()
        q1(s,i+1)
    elif s[i]=='c':
        stack.append(s[i])
        q2(s,i+1)
def q2(s,i):
    print("=>B ",end='')
    try:
        if s[i-1]=='c' and stack[1]=='c':
            stack.pop()
            q2(s,i+1)
        else:
            print("not poping")
    except IndexError as e:
        pass
    finally:
        if i==len(s):
            q3(s)
    
def q3(s):
    print("=>C ")
    if stack[0]=='$':
        print(f"{s} is accepted.")
    else:
        print(f"{s} is not accepted.")
print("State")
q1('abc')
# q1('abcc')
# q1('abbc')
print("State")
q1('aabbcc')
print("State")
q1('aaabbbccc')