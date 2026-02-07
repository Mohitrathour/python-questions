def calculate(a,x):
    c=a.count(x)
    return (c)
a=[]
for i in range(0,10):
    n=int(input(" "))
    a.append(n)
x=int(input("enter a no"))
c=calculate(a,x)
print("frequency=",c)
