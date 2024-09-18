#creating a complex number
x=complex(1,-2)
print("1st complex number: ",x)
#user defined complex number
a=int(input("real part: "))
b=int(input("Imag part: "))
y=complex(a,b)
print("2nd complex number: ",y)

#addition
a=x+y
print(f"\nAddition of {x} and {y} is:= {a}")
#subtraction
b=x-y
print(f"Subtraction of {x} and {y} is:= {b}")
#multiplication
c=x*y
print(f"multiplication of {x} and {y} is:= {c}\n")

#conjugate
cx=x.conjugate()
print(f"conjugate of {x} is:= {cx}")
cy=y.conjugate()
print(f"conjugate of {y} is:= {cy}")


import matplotlib.pyplot as p
x=[1,-2,3,4]
y=[3,-1,2,5]
p.scatter(x,y,color='red')
p.title("Complex numbers ploting")
p.plot(x,y)
p.show()

def rotate():
    s={3+3j,4+3j,2-1j,-5+1j,-2-1j}
    print("\nThe given set of complex number\n",s)
    angle=int(input("Enter the rorating angle: "))
    if angle==90:
        s1={x*1j for x in s}
        print(s1)
        x=[x.real for x in s1]
        y=[x.imag for x in s1]
        p.plot(x,y,'ro')
        p.title("ploting of rotating 90deg")
        p.axis([-6,6,-6,6])
        p.show()
    elif angle==180:
        s1={x*-1j for x in s}
        print(s1)
        x=[x.real for x in s1]
        y=[x.imag for x in s1]
        p.plot(x,y,'ro')
        p.title("ploting of rotating 180deg")
        p.axis([-6,6,-6,6])
        p.show()
    else:
        print("Invalid input\tselect only 90 or 180")
        rotate()
rotate()