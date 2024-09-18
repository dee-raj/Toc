def A(w,i):
    if i==len(w):
        return
    if w[i]=='0':
        print('a',end="")
        B=(w,i+1)
    else:
        print('b',end="")
        A(w,i+1)

def B(w,i):
    if i==len(w):
        return
    if w[i]=='0':
        print('b',end="")
        A=(w,i+1)
    else:
        print('a',end="")
        B(w,i+1)

#main
w='1010'
print("Mealy Machine: \n Input Strings:",w)
print("Output:",end="")
A(w,0)
B(w,0)
