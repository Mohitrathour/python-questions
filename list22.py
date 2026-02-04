a=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input(" "))
    a.append(n)
b=[]
c=[]
for num in a:
    if(num>0):
       b.append(num)
    else:
        c.append(num)
b.extend(c)
print (b)
