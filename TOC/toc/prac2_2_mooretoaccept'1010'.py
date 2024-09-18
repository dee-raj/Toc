def A(w,i):
    print('A/a->',end="")
    if i==len(w):
        return
    if w[i]=='0':
        B(w,i+1)
    else:
        A(w,i+1)

def B(w,i):
    print('B/b->',end="")
    if i==len(w):
        return
    if w[i]=='0':
        B(w,i+1)
    else:
        A(w,i+1)

#main
w='1010'
print("Moore Machine:\n Input String:",w)
print("Output:",end="")
A(w,0)
        
    
