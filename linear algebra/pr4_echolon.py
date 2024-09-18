from sympy import *
row=int(input("Enter row no: "))
col=int(input("Enter col no: "))
A=[]
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input(f"A({i+1},{j+1})= ")))
    A.append(a)
    print()
for i in range(row):
    print("|",end=" ")
    for j in range(col):
        print(A[i][j],end=" ")
    print("|")
m=Matrix(A)
print(m,"\t",A)
row_echolon=m.rref()
print("\nthe row echolon of given matrix: ",row_echolon)

rnk=m.rank()
print("rank of the matrix",rnk)