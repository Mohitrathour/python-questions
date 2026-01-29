l=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input("enter no"))
    l.append(n)
for i in range(0,10):
    if(l[i]%2==0):
        l[i]=0
print("modified list is:",l)          
