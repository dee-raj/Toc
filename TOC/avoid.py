vowel =['a','e','i','o','u']
def q0(s,i=0):
    print("=>A ",end='')
    if i==len(s):
        print(f"[{s}] can't be avoided.")
        return
    if s[i] in vowel:
        q1(s,i+1)
    else:
        q0(s,i+1)
def q1(s,i):
    print("=>B ",end='')
    if i==len(s):
        print(f"[{s}] can't be avoided.")
        return
    if s[i] in vowel:
        q2(s,i+1)
    else:
        q0(s,i+1)
def q2(s,i):
    print("=>C ",end='')
    if i==len(s):
        print(f"[{s}] should be avoided.")
        return
    q2(s,i+1)
print("States of transitions:")
q0('avoid')
q0('sumit')


