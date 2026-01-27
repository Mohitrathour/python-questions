l=[]
for i in range(0,10):
    n=int(input("enter the no"))
    l.append(n)
c=0;p=l[0]
for i in range(1,len(l)):
    if(p==l[i]):
        c+=1
if(c==10):
    print("all no are same")
else:
    print("all are not same")
