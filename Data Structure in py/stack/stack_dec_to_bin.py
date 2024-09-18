class mystack:
    def __init__(self,n):
        self.size=n
        self.items=[]
        self.tos=-1
    def push(self,data):
        assert len(self.items)<self.size, "stack overflow"
        self.items.append(data)
    def show(self):
        self.tos=len(self.items)-1
        print(f"binary of {ab}")
        while self.tos!=-1:
            print(self.items[self.tos])
            self.tos-=1
def dec_to_bin(num):
    s1=mystack(9)
    number=int(num)
    while number>0:
        rem=number%2
        s1.push(str(rem))
        number=number//2
    s1.show()  
#main 
ab=int(input("Enter a number to find binary of it: "))
dec_to_bin(ab)