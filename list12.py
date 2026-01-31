l=[]
print("enter 20 no")
for i in range(0,20):
    n=int(input(" "))
    l.append(n)
c=0;
for i in range(0,20):
    for j in range(1,l[i]+1):
        if(i%j==0):
            c+=1
    if(c==2):
        l[i]=0
print("modified list is:",l)        
    
