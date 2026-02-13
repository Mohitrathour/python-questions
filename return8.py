def prime(n):
    i=1
    c=0
    while(i<=n):
        if(n%i==0):
            c+=1
        i+=1
    if(c==2):
        c=0
        i=1
        return 'true'
    else:
        c=0
        i=1
        return 'false'
for n in range(100,1000):
    a=prime(n)
    if(a=='true'):
        print(n)
