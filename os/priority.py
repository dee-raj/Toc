priority=[]
bt=[]
n=int(input("Enter the no of process: "))
process=[]
for i in range(0,n):
    priority.insert(i,i+1)
bt=list(map(int,input("Enter the burst time: ").split()))
for i in range(0,len(priority)-1):
    for j in range(0,len(priority)-i-1):
        if priority[j]>priority[j+1]:
            temp=priority[j]
            priority[j]=priority[j+1]
            priority[j+1]=temp

            temp=bt[j]
            bt[j]=bt[j+1]
            bt[j+1]=temp
wt=[]
avgwt=0
tat=[]
avgtat=bt[0]
wt.insert(0,0)
tat.insert(0,bt[0])
for i in range(0,len(bt)):
    wt.insert(i,wt[i-1]+bt[i-1])
    tat.insert(i,wt[i]+bt[i])
    avgwt+=wt[i]
    avgtat+=tat[i]
avgwt=float(avgwt)/n
avgtat=float(avgtat)/n
print("Process \t Burst_time \t Waiting_time \t turn-AROUND-time \t Priority")
for i in range(0,n):
    print(str(i)+"\t\t "+str(bt[i])+"\t\t "+str(wt[i])+"\t\t  "+str(tat[i])+"\t\t\t   "+str(priority[i]))
# try:
#     for i in range(0,n):
#         # print(f"{str(process[i])} \t\t {str(bt[i])} \t\t {str(wt[i])} \t\t {str(tat[i])} \t\t {str(priority[i])}")
#         print(str(i)+"\t\t "+str(bt[i])+"\t\t "+str(wt[i])+"\t\t  "+str(tat[i])+"\t\t\t   "+str(priority[i]))
# except Exception as e:
#     print(e)
print("Avg waiting time: "+str(avgwt))
print("Avg turn around time: "+str(avgtat))