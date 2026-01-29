l=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input("enter no"))
    l.append(n)
s=0;j=1,sum=0
for i in range(0,10):
    while(j<=l[i]):
        s+=1
    j+=1
    if(s==2):
        sum=sum+l[i]
    j=1
    c=0
print("sum of prime no is",sum)    
        
        
