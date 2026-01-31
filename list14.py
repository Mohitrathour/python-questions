l=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input("enter no"))
    l.append(n)
rev=0;temp=0;m=1;c=0;sum=0
for i in range(0,len(l)):
    store=l[i]
    while(m<=l[i]):
        if(l[i]%m==0):
            c+=1
        m+=1
    while(store>0):
        temp=store%10
        rev=rev*10+temp
        store=store//10
    if(c!=2 and rev!=l[i]):
        sum=sum+l[i]
    m=1
    rev=0
    temp=0
    c=0
print("sum of non-palprime no is:",sum)        
            
