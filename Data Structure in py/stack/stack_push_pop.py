class mystack:
    def __init__(self,n):
        self.size=n
        self.items=[]
        self.tos=-1
    def count(self):
        return len(self.items)
    def isempty(self):
        return self.items==[]
    def isfull(self):
        return len(self.items)==self.size
    def push(self,data):
        assert len(self.items)<self.size, "stack overflow" 
        self.items.append(data)
        # print(self.items)
        
    def pop(self):
        assert len(self.items)>self.size -1, "stack underflow"
        self.tos=len(self.items)-1
        x=self.items[self.tos]
        self.tos-=1
        return x
phone1=mystack(5)
print(phone1.isempty())
# phone1.pop()
phone1.push("nokiya")
phone1.push("realme")
print(phone1.isfull())
# phone1.push("p")
# phone1.push("d")
# phone1.push("e")
print(phone1.isempty())
# phone1.push("F")
print(f"size of stack is= {phone1.count()}")
print("poped all the iterms from the stack. \n")
phone1.pop()