l=[]
print("enter 10 no")
for i in range(0,10):
    n=int(input("enter no"))
    l.append(n)
c=0;s=l[0];
for i in range(1,10):
    if(s>l[i]):
       c+=1
if(c==10):
     print("all are in decending order")
else:
    print("all are not in decending order")
          
          
