def A(w,i):
    print("A->",end=" ")
    if(i==len(w)):
        print("No")
        return
    if w[i]=="1":
        B(w,i+1)
    else:
        A(w,i+1)
def B(w,i):
    print("B->",end=" ")
    if(i==len(w)):
        print("No")
        return
    if w[i]=="1":
        B(w,i+1)
    else:
        C(w,i+1)
def C(w,i):
    print("C->",end=" ")
    if(i==len(w)):
        print("Yes")
        return
    if w[i]=="1":
        B(w,i+1)
    else:
        C(w,i+1)

#main
s=(input("Enter the String: "))
A(s,0)
        
        
        
        
        
