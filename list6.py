l=[168,25,22,12,4,25,2,15,8,3]
c=0
for i in range(0,len(l)):
    if(l[i]%2==0):
        c+=1
if(c==10):
    print("all are even")
else:
    print("all are not even")
