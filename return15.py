def isprime(n):
    i=1
    c=0
    while(i<=n):
        if(n%i==0):
            c+=1
        i+=1
    if(c==2):
        i=1
        c=0
        return 'true'
    else:
        i=1
        c=0
        return 'false'
def reverse(n):
    i1=1
    c1=0
    temp=0
    rev=0
    while(n>0):
        temp=n%10
        rev=rev*10+temp
        n=n//10
    while(i1<=rev):
        if(rev%i1==0):
            c1+=1
        i1+=1
    if(c1==2):
        i1=1
        c1=0
        temp=0
        rev=0
        return 'true'
    else:
        i1=1
        c1=0
        temp=0
        rev=0
        return 'false'
print("enter 10 no")
s=0
for i in range(1,11):
    n=int(input("enter no"))
    b=isprime(n)
    m=reverse(n)
    if(b=='true' and m=='true'):
        s=s+n
print("sum of twisted prime no:",s)        
        
        
