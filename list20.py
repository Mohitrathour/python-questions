def list(l,a):
    s=[]
    sum=0
    for i in range(0,5):
        sum=l[i]+a[i]
        s.append(sum)
    return (s)
l=[]
a=[]
for i in range(0,5):
    n=int(input("enter the no to inserted in list 1"))
    m=int(input("enter the no to inserted in list 2"))
    l.append(n)
    a.append(m)
b=list(l,a)
print("modified list:",b)
