def rectangle(l,b):
    area=l*b
    return (area)
def square(s):
    area=s*s
def circle(r):
    area=3.14*(r**2)
print("1. area of reactangle")
print("2.area of square")
print("3.area of circle")
ch=int(input("enter your choice"))
if(ch==1):
    l=int(input("enter length"))
    b=int(input("enter breath"))
    r=rectangle(l,b)
    print(r)
elif(ch==2):
    s=int(input("enter side"))
    m=square(s)
    print(m)
elif(ch==3):
    r=int(input("enter radius"))
    c=circle(r)
    print(c)
    
