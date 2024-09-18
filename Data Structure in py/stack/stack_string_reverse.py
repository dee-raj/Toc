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
            print(self.items[self.tos],end='')
            self.tos-=1
def string_reverse(s):
    x=len(s)
    s1=mystack(x)
    for i in s:
        s1.push(i)
    s1.show()
mc=mystack(10)
sr="ALGORITHM"
mc.push(sr)
mc.show()
print("\nReversed string using stack:-")
string_reverse(sr)