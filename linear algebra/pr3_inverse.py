import numpy as np
dim=int(input("Enter row and column: "))
matrix=[]
print("Emter elements:")
for i in range(dim):
    a=[]
    for j in range(dim):
        a.append(int(input(f"A({i+1},{j+1})=")))
    matrix.append(a)
    print()
for i in range(dim):
    print("|",end=" ")
    for j in range(dim):
        print(matrix[i][j],end=" ")
    print("|")

x=np.linalg.det(matrix)
import math
print(f"Determinantof the matrix is={x:.2f}\n")
if x!=0 :
    print("The matrix is invertible.\nInverse of the matrix does exist.")
    # print(f"Determinantof the matrix is={x:.4f}\nThe matrix is invertible.")
    # print(f"Determinantof the matrix is={math.ceil(x)}\nThe matrix is invertible.")
    inverse=np.linalg.inv(matrix)
    print(inverse)
else:
    print("THe matrix is not invertible\nInverse of the matrix doesn't exist.")