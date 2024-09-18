bt=[]
print("Enter the num of process:")
n=int(input())
print("Enter the burst time of process:")
bt=list(map(int,input().split(" ")))
wt=[]
avgwt=0
avgtat=bt[0]
tat=[]
wt.insert(0,0)
tat.insert(0,bt[0])
for i in range (0,bt[0]):
    wt.insert(i,wt[i-1]+bt[i-1])
    tat.insert(i,wt[i]+bt[i])
    avgwt+=wt[i]
    avgtat+=tat[i]
avgwt=float(avgwt)/n
avgtat=float(avgtat)/n
print("process \t Burst time \t Waiting time \t Turn around time")
for i in range(0,n):
    print(str(i)+"\t"+str(bt[i])+"\t"+str(wt[i])+"\t"+str(tat[i]))
    print("\n")
print("Avg Waiting time:",avgwt)
print("Avg Turn around time:",avgtat)