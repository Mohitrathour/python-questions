l=[]
n=100
i=1;rev=0;temp=0
j=1
c=0
while(i<=20 and n<=999):  
    while(j<=n):
      if(n%j==0):
        c+=1
      j+=1
    store2=n    
    while(store2>0):
        temp=store2%10
        rev=rev*10+temp
        store2=store2//10   
    if(c==2 and rev==n):
        l.append(n)
        i+=1
    rev=0
    temp=0
    c=0
    n+=1
    j=1
print(l)
