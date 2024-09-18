class mystack:
    def __init__(self,n):
        self.size=n
        self.items=[]
        self.tos=-1
    def count(self):
        return len(self.items) 
    def isfull(self):
        return len(self.items)==self.size
    def isempty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        self.tos=len(self.items)-1
        while self.tos!=-1:
            print(self.items[self.tos])
            self.tos-=1
    def show(self):
        self.tos=len(self.items)-1
        while self.tos!=-1:
            print(self.items[self.tos])
            self.tos-=1
subject=mystack(7)
print(f"\nthe length of stack: {subject.count()}\n")
print(f"\nIs the stack full: {subject.isfull()}\n")
subject.pop()
print(f"\nIs the stack empty: {subject.isempty()}\n")