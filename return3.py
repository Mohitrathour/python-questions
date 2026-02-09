def calculate(h,m,s):
    hours=h*60*60
    minutes=m*60
    seconds=s
    total=hours+minutes+seconds
    return (total)
a=int(input("enter the hours"))
b=int(input("enter the minutes"))
c=int(input("enter the seconds"))
m=calculate(a,b,c)
print("total seconds:",m)
