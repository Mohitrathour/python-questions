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
def ispalin(n):
    temp=0
    rev=0
    store=n
    while(store>0):
        temp=store%10
        rev=rev*10+temp
        store=store//10
    if(rev==n):
        return 'true'
    else:
        return 'false'
n=int(input("enter a no"))
prime=isprime(n)
palin=ispalin(n)
if(prime=='true' and palin=='true'):
    print("its a palindrom no")
else:
    print("its not a palindrom no")
    
    
        
