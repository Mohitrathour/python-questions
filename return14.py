def isspy(n):
    temp=0
    s=0
    p=1
    while(n>10):
        temp=n%10
        s=s+temp
        p=p*temp
        n=n//10
    if(s==p):
        temp=0
        s=0
        p=1
        return 'true'
    else:
        temp=0
        s=0
        p=1
        return 'false'
print("enter 10 no")
s=0
for i in range(1,11):
    n=int(input("enter no"))
    b=isspy(n)
    if(b=='true'):
        s=s+n
print("sum of spy no",s)        
