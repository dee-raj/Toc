p=int(input("Enter no of process:"))
bt=[]
ts=int(input("Enter tims slice:"))
for i in range(p):
	n=int(input("Enter The burst time:"))
	bt.append(n)
sbt=1
rt=[]
wt=[]
ut=[]
empty=0
tat=[]
while(sbt!=0):
	sbt=0
	print("Burst time is:",bt)
	for i in range(p):
		if(bt[i]>ts):
			rts=bt[i]-ts
			rt.insert(i,rts)
			wt.append(rt[i])
			bt[i]=rt[i]
			ut.append(ts)
			sbt=sbt+bt[1]
		else:
			rt.insert(i,0)
			wt.append(rt[i])
			ut.append(bt[i])
			bt[i]=rt[i]
			sbt=sbt+bt[i]
print("Waiting time is:",wt)
print("Used time is:",ut)
for i in range(len(ut)):
	tat.append(empty)
	empty=ut[i]
print("Turn around time :",tat)
process_exe=[]
for i in range(len(tat)):
	if (ut[i-1]!=0):
		process_exe.append(tat[i])
	else:
		process_exe.append(0)
for x in range(0,len(process_exe),p):
	chunks=[process_exe[x:x+p]]
	print(chunks)
i=0
roundstart=0
roundend=0
while i<len(chunks):
	j=0
	while j>0:
		roundstart(chunks[i][j])
		print("p"+str[j]-startat,roundstart)
		j=j+1
	i=i+1
