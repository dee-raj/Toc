a=[1,2,3,4,5,3]
n=len(a)
m=3
def lru():
    global a,m,n
    x=0
    pfault=0
    p=[]
    phit=0
    for i in range(m):
        p.append(-1)
    for i in range(n):
        f=0
        for j in range(m):
            if (p[j]==a[i]):
                f=1
                break
        if(f==0):
            if(p[x]!=-1):
                min=999
                for k in range(m):
                    f=0
                    j=1
                    while j>=0:
                        j-=1
                        if(p[k]==a[j]):
                            f=1
                            break
                            if(f==1 and min>j):
                                min=j
                                x=k
                            else:
                                print("\n %d d->pagehit"%a[i])
                                phit+=1
                                    
        p[x]=a[i]
        x=(x+1)%m
        pfault+=1
        print("\n %d-> "%(a[i]))
        for j in range(m):
            
                        if(p[j]!=-1):
                            print(p[j])
                        else:
                            print("___")
                                
    print("\n Total page fault : %d"%(n-phit-1))
    print("\n Total page hits : %d"%(phit+1)) 
lru()
