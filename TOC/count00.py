_00=0
def q1(s,i):
    if i==len(s):
        print("Q1\nNo input symbol is given.")
        return
    print("Q1=> ",end='')
    if s[i]=='0':
        q3(s,i+1)
    else:
        q2(s,i+1)

def q2(s,i):
    if i==len(s):
        print(f"\nNo of 00 in {s} is= {_00}")
        return
    print("Q2=> ",end='')
    if s[i]=='0':
        q3(s,i+1)
    else:
        q2(s,i+1)
        
def q3(s,i):
    if i==len(s):
        print(f"\nNo of 00 in {s} is= {_00}")
        return
    print("Q3=> ",end='')
    if s[i]=='0':
        q4(s,i+1)
    else:
        q2(s,i+1)
        
def q4(s,i):
    global _00
    _00+=1
    if i==len(s):
        print(f"\nNo of 00 in {s} is= {_00}")
        return
    print("Q4=> ",end='')
    if s[i]=='0':
        q3(s,i+1)
    else:
        q2(s,i+1)

w='1010010011'
# w=''
print(f"transition of states for [{w}] is/are:",end='\t')
q1(w,0)