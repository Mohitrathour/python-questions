l=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input("enter no"))
    l.append(n)
temp=0;rev=0;m=1;n=1;a=0;b=0;sum=0
for i in range(0,len(l)):
    store=l[i]
    while(store>0):
        temp=store%10
        rev=rev*10+temp
        store=store//10
    while(m<=l[i]):
        if(l[i]%m==0):
            a+=1
        m+=1
    while(n<=rev):
        if(rev%n==0):
            b+=1
        n+=1
    if(m==2 and n==2):
        sum=sum+l[i]
    m=1
    n=1
    a=0
    b=0
    temp=0
    rev=0
print("sum of twisted prime no is:",sum)    
    
            
            
