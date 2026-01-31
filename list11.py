l=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input(" "))
    l.append(n)
sum=0;c=0
for i in range(0,10):
    for j in range(1,l[i]+1):
        if(i%j==0):
            c+=1
    if(c==2):
        sum=sum+l[i]
    c=0
print("sum of prime no is:",sum)    
