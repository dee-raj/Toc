import numpy as np
n_list=4
u=np.array([-3,0,3,4])
print("Vactor u= ",u)

v=np.array([4,5,6,-3])
print("vector v= ",v)

a=int(input("Enter number: "))
b=int(input("Enter number: "))
op=a*u+b*v

print(a*u)
print(b*v)
print(op)

print(np.dot(u,v))