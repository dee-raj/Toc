class stack:
    def __init__(self):
        self.stack=['$']
    def push(self,data):
        self.stack.insert(0,data)
    def pop(self):
        self.stack.pop(0)
obj=stack()
def q0(str,idx=0):
    if str[idx] =='1' or str[idx]=='0':
        obj.push(str[idx])
        q0(str,idx+1)
    else:
        q1(str,idx+1)
def q1(str,idx):
    if idx==len(str):
        # print(obj.stack)
        if obj.stack[0]=='$':
            print("accepted")
        else:
            print("not allowed")
    elif str[idx] == obj.stack[0]:
        obj.pop()
        q1(str,idx+1)
    elif str[idx]!= obj.stack[0]:
        print('not interested')
q0('010$01')