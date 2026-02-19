def seconds(h,m,s):
    hours=h*60*60
    minutes=m*60
    second=s
    total=hours+minutes+seconds
    print("total seconds:",total)
h=int(input("enter hours"))
m=int(input("enter the minutes"))
s=int(input("enter seconds"))
seconds(h,m,s)
