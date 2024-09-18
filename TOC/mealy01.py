"""
    0 o/p  1 o/p
A   B a    A b
B   A b    B a
"""
def A(s,i=0):
    if i==len(s):
        return
    print("A-> ",end='')
    if s[i]=='1':
        print('with o/p =>b')
        A(s,i+1)
    else:
        print('with o/p =>a')
        B(s,i+1)
def B(s,i):
    if i==len(s):
        return
    print("B-> ",end='')
    if s[i]=='0':
        print('with o/p =>b')
        A(s,i+1)
    else:
        print('with o/p =>a')
        B(s,i+1)
w='100101'
A(w)