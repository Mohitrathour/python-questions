def spy(n):
    temp=0
    s=0
    p=1
    while(n>0):
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
a=int(input("enter the lower limit "))
b=int(input("enter the upper limit"))
for i in range(a,b):
    d=spy(i)
    if(d=='true'):
        print(i)
