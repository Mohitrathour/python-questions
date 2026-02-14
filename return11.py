is twinprime(n):
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
for i in range(1,100):
    a=twinprime(i)
    b=twinprime(i+2)
    if(a=='true' and b=='true'):
        print(i,'\t' ,(i+2))
