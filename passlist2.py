def check(l):
    for i in range(0,10):
        if(l[i]%2==0):
            l[i]=0
    return (l)
print("enter 10 no")
l=[]
for i in range(1,11):
    n=int(input("enter no"))
    l.append(n)
b=check(l)
print("modified list:",l)
