def calculate(radius,height):
    v=3.14*radius**2*height
    tsa=2*3.14*radius*height+2*3.14*radius**2
    print("volume:",v)
    print("total surface area:",tsa)
a=float(input("enter the radius"))
b=float(input("enter the height"))
calculate(a,b)
