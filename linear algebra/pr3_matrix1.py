rowa=int(input("a> Enter rows no: "))
cola=int(input("a> Enter col no: "))
matrix1=[]
print("Enter elements of a")
for i in range(rowa):
    temp=[]
    for j in range(cola):
        temp.append(int(input(f"A({i+1},{j+1})= ")))
    matrix1.append(temp)
    print()
print("\nMatrix A")
for i in range(rowa):
    print("|",end=" ")
    for j in range(cola):
        print(matrix1[i][j],end="  ")
    print("|")

rowb=int(input("b> Enter rows no: "))
colb=int(input("b> Enter col no: "))
matrix2=[]
print("Enter elements of b")
for i in range(rowb):
    temp=[]
    for j in range(colb):
        temp.append(int(input(f"B({i+1},{j+1})= ")))
    matrix2.append(temp)
    print()
print("\nMatrix B")
for i in range(rowb):
    print("|",end=" ")
    for j in range(colb):
        print(matrix2[i][j],end="  ")
    print("|")

#Addition
# if (rowa==rowb) & (cola == colb):
#     print("\nAddition of A and B")
#     for i in range(rowa):
#         print("|",end=" ")
#         for j in range(cola):
#             print(matrix1[i][j]+matrix2[i][j],end=" ")
#         print("|")
# else:
#     print("\nwrong inputs......!\nCan not add two matrix of diff order.")


result=[]
for i in range(cola):
    d=[]
    for j in range(colb):
        d.append(0)
    result.append(d)
#multiply
if cola==rowb:
    print("\nMultiplication")
    for i in range(rowa):
        for j in range(colb):
            for k in range(cola):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
    #printing
    for i in range(rowa):
        for j in range(colb):
            print(result[i][j],end=" ")
        print()
