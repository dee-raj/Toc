import numpy as np
dim=int(input("Enter the dimension of a square matrix: "))
A=[]
print("-> Enter the elements of the Matrix:")
for i in range(dim):
    a=[]
    for j in range(dim):
        a.append(int(input(f"A({i},{j})=")))
    A.append(a)
print("\nMatrix A")
for row in range(dim):
    print("[",end=" ")
    for col in range(dim):
        print(A[row][col],end=" ")
    print("]")
print("\n")
row1,col2=np.linalg.eig(A)
print(f"E_Value= {row1}\nE_Value= {col2}")
