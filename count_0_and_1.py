one=zero=0
def A(s,i):
    global one,zero
    if i==len(s):
        # print(f"\nTotal no.of 0's are=>{zero}.\nTotal no.of 1's are=>{one}.")
        print("A\nstring must contain a symbol")
        return
    print("A=> ",end='')
    if s[i]=='0':
        zero+=1
        B(s,i+1)
    else:
        one+=1
        C(s,i+1)
    
def B(s,i):
    global one,zero
    if i==len(s):
        print(f"\nTotal no.of 0's are=>{zero}.\nTotal no.of 1's are=>{one}.")
        return
    print("B=> ",end='')
    if s[i]=='0':
        zero+=1
        B(s,i+1)
    else:
        one+=1
        C(s,i+1)
    
def C(s,i):
    global one,zero
    if i==len(s):
        print(f"\nTotal no.of 0's are=>{zero}.\nTotal no.of 1's are=>{one}.")
        return
    print("C=> ",end='')
    if s[i]=='0':
        zero+=1
        C(s,i+1)
    else:
        one+=1
        B(s,i+1)
w='1010110011'
print(f"transition states of [{w}] string are:  ",end='')
A(w,0)
print(f"total length of string: {one+zero}")