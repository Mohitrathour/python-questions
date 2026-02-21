def last(x,y,z):
    temp1=x%10
    temp2=y%10
    temp3=z%10
    return(temp1,temp2,temp3)
x=int(input("enter first no"))
y=int(input("enter second no"))
z=int(input("enter third no"))
a,b,c=last(x,y,z)
s=a+b+c
print("sum of last digits of these no are:",s)
