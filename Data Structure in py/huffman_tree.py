#a huffman tree node
class node:
    def __init__(self,freq,symbol,right=None,left=None):
        self.freq=freq
        self.right=right
        self.left=left
        self.huff=''
        self.symbol=symbol
def printNode(node,val=''):
    newval=val+str(node.huff)
    if node.left:
        printNode(node.left,newval)
    if node.right:
        printNode(node.right,newval)
    if not node.right and not node.left:
        print(f"{node.symbol} -> {newval}")

#chars=["a","b","c","d","e","f"]
#freq=[5,9,12,13,16,45]
#chars=['a','b','d','h','j','r','u'] #dhurbaraj
#freq=[2,1,1,1,1,2,1]
chars=["s","h","e","l","a","o","n","t","r"]
freq=[8,4,7,4,2,2,1,1,1]
nodes=[]
for x in range(len(chars)):
    nodes.append(node(freq[x],chars[x]))
while len(nodes )>1:
    nodes=sorted(nodes,key=lambda x:x.freq)
    left=nodes[0]
    right=nodes[1]
    

    left.huff=0
    right.huff=1
    newval=node(left.freq+right.freq,left.symbol,left,right)

    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newval)
printNode(nodes[0])
