def calculate():
    p=int(input("enter the principal"))
    r=int(input("enter the rate"))
    t=int(input("enter the time"))
    si=(p*r*t)/100
    return (si)
a=calculate()
print("simple interest:",a)
