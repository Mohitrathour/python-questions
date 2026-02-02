l=[]
i=1
j=1
n=1
c=0
while(i<=20):
    while(j<=n):
        if(n%j==0):
            c+=1
        j+=1   
    if(c==2):
        l.append(n)
        i+=1
    c=0
    n+=1
    j=1
print("list of first 20 prime no is:",l)    
            
