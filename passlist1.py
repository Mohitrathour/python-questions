def calculate(a):
    l=a[0];s=a[0]
    for i in range(1,20):
        if(l<=a[i]):
            l=a[i]
        if(s>=a[i]):
            s=a[i]
        avg=(s+l)/2
        return (avg)
a=[]
print("enter 20 no")
for i in range(1,21):
    n=int(input("enter no"))
    a.append(n)
b=calculate(a)
print("average=",b)
