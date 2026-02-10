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
a=int(input("enter a no"))
b=ispalin(a)
if(b=='true' or b=='TRUE'):
    print("its a palindrom no")
else:
    print("its not a palindrom no")
    
