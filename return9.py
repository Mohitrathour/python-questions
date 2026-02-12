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
def ispalin(n):
    temp=0
    rev=0
    store=n
    while(store>0):
        temp=store%10
        rev=rev*10+temp
        store=store//10
    if(rev==n):
        temp=0
        rev=0
        store=0
        return 'true'
    else:
        temp=0
        rev=0
        store=0
        return 'false'
for n in range(100,1000):
    b=isprime(n)
    c=ispalin(n)
    if(b=='true' and c=='true'):
        print(n)
