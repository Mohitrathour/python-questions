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
print("enter 10 no")
s=0
for i in range(1,11):
    n=int(input("enter no"))
    b=ispalin(n)
    if(b=='true'):
        s=s+n
print("sum of palindrom no are:",s)        
