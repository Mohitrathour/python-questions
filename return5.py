def isprime(n):
    i=1
    c=0
    while(i<=n):
        if(n%i==0):
            c+=1
        i+=1
    if(c==2):
        return 'true'
    else:
        return 'false'
a=int(input("enter a no"))
b=isprime(a)
if(b=='true' or b=='TRUE'):
    print("its a prime  no")
else:
    print("its not a prime no")
