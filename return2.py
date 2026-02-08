def small(a,b,c):
    if(a<b and a<c):
        return (a)
    elif(b<a and b<c):
        return (b)
    elif(c<a and c<b):
        return (c)
a=int(input("enter first no"))
b=int(input("enter second no"))
c=int(input("enter third no"))
smallest=small(a,b,c)
print("smallest no is:",smallest)
