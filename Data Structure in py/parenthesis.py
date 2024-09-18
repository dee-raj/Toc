open_list=['(','{','[']
close_list=[')','}',']']
#function to check paranthesis
def check(mystr):
    stack=[]
    for i in mystr:
        if i in open_list:
            stack.append(i)
            # print('push into stack: ',stack)
        elif i in close_list:
            pos=close_list.index(i)
            if (len(stack)>0 and (open_list[pos]==stack[len(stack)-1])):
                stack.pop()
            else:
                return "checked and found unbalanced paranthesis\n"
            # print("After pop",stack[::-1])
    if len(stack)==0:
        return "balanced"
    else:
        return "Unbalanced not working" 
#driver
s="[{([a])]"
print(f"{s} - {check(s)}")
s="[([{}])]"
print(f"{s} - {check(s)}") 