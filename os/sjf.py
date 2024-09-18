bt=[]
print("enter the no of process")
n=int(input())
process=[]
for i in range(0,n):
        process.insert(i,i+1)
print("enter the burst time of process")
bt=list(map(int,input().split()))
for i in range(0,len(bt)-1):
        for j in range(0,len(bt)-i-1):
                if(bt[j]>bt[j+1]):
                   temp=bt[j]
                   bt[j]=bt[j+1]
                   bt[j+1]=temp
                   temp=process[j]
                   process[j]=process[j+1]
                   process[j+1]=temp
wt=[]
avgwt=0
avgtat=bt[0]
tat=[]
wt.insert(0,0)
tat.insert(0,bt[0])
for i in range(1,len(bt)):
        wt.insert(i,wt[i-1]+bt[i-1])
        tat.insert(i,wt[i]+bt[i])
        avgwt+=wt[i]
        avgtat+=tat[i]
avgwt=float(avgwt)/n
avgwt=float(avgtat)/n
print("process \t burst time \t waiting time\t turn around time")
for i in range(0,n):
        print(str(process[i])+"\t"+str(bt[i])+"\t"+str(wt[i])+"\t"+str(tat[i]))
        print("\n")
print("avg waiting vtime:",avgwt)
print("avg turn around time",avgtat)
                   
