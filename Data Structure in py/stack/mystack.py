import timeit
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
		assert len(self.items)<self.size,"stack overflow"
		self.items.append(data)
	def pop(self):
		assert len(self.items)>self.size-1,"stack underflow"
		self.tos=len(self.items)-1
		x=self.items[self.tos]
		self.tos=self.tos-1
		return x
	def show(self):
		self.tos=len(self.items)-1
		while self.tos !=-1:
			print(self.items[self.tos])
			self.tos=self.tos-1
#main
phones=mystack(10)
phones.push("Iphone")
phones.push("samsung")
phones.push("Oppo")
phones.push("Poco")
phones.push("Vivo")
phones.push("Nokia")
phones.push("MI")
phones.push("One plus")
phones.push("redme")
phones.push("realme")
phones.pop()
phones.show()
print("ISfull\n",phones.isfull())
print("ISempty\n",phones.isempty())

#2nd
def string_reverse(s):
	x=len(s)
	s1=mystack(x)
	for i in s:
		s1.push(i)
	s1.show()
print(string_reverse("ALGORITHM"))
#3rd
def is_palindrome(s):
	x=len(s)
	# s1=mystack(x)
	x=x-1
	reverse=""
	while x>=0:
		reverse=reverse+s[x]
		x=x-1
	if s==reverse:
		print(s," is a palindrome.")
		return True
	else:
		print(s,"is not a palindrome.")
		return False
print(is_palindrome("liril"))
print(is_palindrome("apple"))

#4th]
import timeit as t
def dec_to_bin(s):
	print("The binary of ",s,"is: ")
	s1=mystack(10)
	n=int(s)
	while n>0:
		rem=n%2
		s1.push(str(rem))
		n=n//2
	s1.show()

print(dec_to_bin(56))
print("TIME1: ",timeit.timeit())
print("TIME2: ",t.timeit())