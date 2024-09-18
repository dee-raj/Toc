# """
#     0   1   o/p
# A   B   A   a
# B   B   A   b
# """

# def A(s,i=0):
#     print("A-> with o/p =>a")
#     if i==len(s):
#         return
#     if s[i]=='1':
#         A(s,i+1)
#     else:
#         B(s,i+1)
# def B(s,i):
#     print("B-> with o/p =>b")
#     if i==len(s):
#         return
#     if s[i]=='0':
#         B(s,i+1)
#     else:
#         A(s,i+1)
# w='10011'
# A(w)




one=zero=0
def count10(s,i=0):
    global one,zero
    if i==len(s):
        print(f"\nNo of 1's={one} & 0's={zero} in [ {s} ]")
        return
    if s[i]=='1':
        one +=1
        count10(s,i+1)
    else:
        zero +=1
        count10(s,i+1)
    return one,zero
# w='100010101'
# count10(w)
count10('10001011')