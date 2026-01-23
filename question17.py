#Q17: Write a program to find the roots of a quadratic equation and categorize them.

a=int(input("enter the cofficient of x^2"))
b=int(input("enter the cooficient of x"))
c=int(input ("enter the value of c"))
import math
x=(-b+(math.sqrt(b**2-4*a*c)))//2*a
x2=(-b-(math.sqrt(b**2-4*a*c)))//2*a
d=b**2-4*a*c
if(d>0):
    print("root are real and different:",x,x2)
elif(d<0):
    print("roots are complex")
else:
    print("roots are real and same:",x)
            
            
