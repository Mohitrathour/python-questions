def calculate(l,b):
    area=l*b
    perimeter=2*(l+b)
    return area,perimeter
a=int(input("enter the length"))
b=int(input("enter the breath"))
x,y=calculate(a,b)
print("area of rectangle is:",x)
print("perimeter of rectangle is:",y)
