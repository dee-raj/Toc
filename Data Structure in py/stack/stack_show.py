class mystack:
    def __init__(self,n):
        self.size=n
        self.items=[]
        self.tos=-1

    def push(self,data):
        assert len(self.items)<self.size, "strack overflow"
        self.items.append(data)
    def show(self):
        self.tos=len(self.items)-1
        while self.tos!=-1:
            print(self.items[self.tos])
            self.tos-=1
phone=mystack(4)
phone.push("one plush 1")
phone.push("one plush 5/5t")
phone.push("poco M2")
phone.push("Mi note 9s/9 pro")
phone.show()