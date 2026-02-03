def calculate(l):
    for i in range(1,11):
        i=1
        c=0
        while(i<=l[i]):
            if(l[i]%i==0):
                c+=1
            i+=1
        if(c==2):
            l[i]=0
        i=1
        c=0
    return (l)
l=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input("enter no"))
    l.append(n)
b=calculate(l)
print("modified list:",l)
    
