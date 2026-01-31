l=[]
print("enter 20 no ")
for i in range(0,20):
    n=int(input("enter no"))
    l.append(n)
s=0;p=1;sum=0
for i in range(0,len(l)):
    store=l[i]
    while(store>0):
        temp=store%10
        p=p*temp
        s=s+temp
        store=store//10
    if(p==s):
        sum=sum+l[i]
    s=0
    p=1
print("sum of all the spy no is:",sum)    
