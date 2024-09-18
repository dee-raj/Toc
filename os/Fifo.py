a=[1,2,3,4,5,6,1,2,3,6,5]
n=len(a)
m=3
def fifo():
	global a,m,n
	f=-1
	pagefault=0
	page=[]
	for i in range(m):
		page.append(-1)
	for i in range(n):
		flag=0
		for j in range(m):
			if (page[j]==a[i]):
				flag=1
				break
		if(flag==0):
			f=(f+1)%m
			page[f]=a[i]
			pagefault+=1
			print("\n\n%d -> "%a[i])
			for j in range(m):
				if(page[j]!=-1):
					print(page[j],end=" ")
				else:
					print("___")
		else:
			print("\n %d -> No page Fault"%a[i])
	print("\n Total Page Fault:%d"%(pagefault))
fifo()