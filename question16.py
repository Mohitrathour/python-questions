#Q16: Write a program to input three numbers and find the largest among them using if–else.


a=int(input("enter first no"))
b=int(input("enter second no"))
c=int(input("enter third no"))
if(a>b and a>c):
    print("largest is",a)
elif(b>a and b>c):
    print("largest is",b)
else:
    print("largest is:",c)
