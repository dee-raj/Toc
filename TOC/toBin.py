def makeBinary(num):
    temp=0
    while num>0:
        temp=num%2
        num=num//2
        print(temp,end='')
makeBinary(21)

def makeDeci(bin):
    print(end='\n')
    return int(bin,2)
print(makeDeci("10101"))    
