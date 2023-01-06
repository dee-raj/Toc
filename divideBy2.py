#the input number in binary format is divisible by 2 or not 
def q0(s,i):
  print("Q0=> ",end='')
  if i==len(s):
    print("not final state, number is not divisible by 2")
    return
  if s[i]=='0':
    q0(s,i+1)
  else:
    q2(s,i+1)

def q1(s,i):
  print("Q0=> ",end='')
  if i==len(s):
    print("not final state, number is not divisible by 2")
    return
  if s[i]=='0':
    q1(s,i+1)
  else:
    q2(s,i+1)

def q2(s,i):
  print("Q0=> ",end='')
  if i==len(s):
    print("not final state, number is not divisible by 2")
    return
  if s[i]=='0':
    q1(s,i+1)
  else:
    q2(s,i+1)
w='101101'
w='0010010'
print(f"is '{w}' divisible by 2?")
q1(w,0)
