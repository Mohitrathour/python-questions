def rectangle(l,b):
    perimeter=2*(l+b)
    return (perimeter)
def square(s):
    perimeter=4*s
    return (perimeter)
def circle(r):
    circumference=2*3.14*r
    return (circumeference)
print("1.perimeter of rectangle")
print("2.perimeter of square")
print("3.circumference of circle")
ch=int(input("enter your choice"))
if(ch==1):
    l=int(input("enter the length"))
    b=int(input("enter the breath"))
    r=rectangle(l,b)
    print(r)
elif(ch==2):
    s=int(input("enter the side"))
    a=square(s)
    print(a)
elif(ch==3):
    r=int(input("enter the radius"))
    b=circle(r)
    print(b)
    
