class mystack:
    def __init__(self,n):
        self.size=n
        self.items=[]
        self.tos=-1
    def count(self):
        return len(self.items)
    def push(self,data):
        assert len(self.items)<self.size, "stack overflow"
        self.items.append(data)
phone1=mystack(3)
phone1.push("nokiya")
phone1.push("realme")
phone1.push("poco X3")
print("Total no of items in the stack: ",phone1.count())