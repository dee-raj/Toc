
def A(w,i,z,c):
    
    if i==len(w):
        print("1's are ",z)
        print("0's are ",c)
        print("No")
        return
    if w[i]=='1':
        z=z+1
        C(w,i+1,z,c)
    else:
        c=c+1
        B(w,i+1,z,c)

def B(w,i,z,c):
    
    if i==len(w):
        print("1's are ",z)
        print("0's are ",c)
        print("Yes")
        return
    if w[i]=='1':
        z=z+1
        C(w,i+1,z,c)
    else:
        c=c+1
        B(w,i+1,z,c)

def C(w,i,z,c):
    
    if i==len(w):
        print("1's are ",z)
        print("0's are ",c)
        print("yes")
        return
    if w[i]=='1':
        z=z+1
        C(w,i+1,z,c)
    else:
        c=c+1
        B(w,i+1,z,c)


#main
str="0100010111"
A(str,0,0,0)



 
